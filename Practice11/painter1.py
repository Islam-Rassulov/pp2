import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    # Added new hotkeys to the caption for clarity
    pygame.display.set_caption("Paint: [B]rush, [R]ect, [S]quare, [C]ircle, [T]riangle, [Q]uilateral, [M]hombus, [E]raser")
    clock = pygame.time.Clock()
    
    radius = 15
    drawing = False
    tool = 'brush' 
    curr_color = (0, 0, 255) 
    
    elements = []
    start_pos = None

    while True:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                # --- Tool Selection ---
                if event.key == pygame.K_b: tool = 'brush'
                if event.key == pygame.K_r: tool = 'rect'
                if event.key == pygame.K_s: tool = 'square'
                if event.key == pygame.K_c: tool = 'circle'
                if event.key == pygame.K_t: tool = 'right_tri'
                if event.key == pygame.K_q: tool = 'eq_tri'
                if event.key == pygame.K_m: tool = 'rhombus' # 'M' for Rhombus
                if event.key == pygame.K_e: 
                    tool = 'brush'
                    curr_color = (0, 0, 0) 
                
                # --- Color Selection ---
                if event.key == pygame.K_1: curr_color = (255, 0, 0)
                if event.key == pygame.K_2: curr_color = (0, 255, 0)
                if event.key == pygame.K_3: curr_color = (0, 0, 255)
                if event.key == pygame.K_4: curr_color = (255, 255, 0)
                if event.key == pygame.K_5: curr_color = (255, 255, 255)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                if tool == 'brush':
                    elements.append({'type': 'brush', 'color': curr_color, 'pos': event.pos, 'radius': radius})

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing and tool != 'brush':
                    # Save the shape with its start and end points
                    elements.append({'type': tool, 'color': curr_color, 'start': start_pos, 'end': event.pos})
                drawing = False

            if event.type == pygame.MOUSEMOTION:
                if drawing and tool == 'brush':
                    elements.append({'type': 'brush', 'color': curr_color, 'pos': event.pos, 'radius': radius})

        # --- Drawing Logic ---
        # Draw all stored elements from the list
        for ent in elements:
            draw_shape(screen, ent)

        # Draw visual feedback (ghost shape) while dragging
        if drawing and tool != 'brush':
            current_mouse = pygame.mouse.get_pos()
            temp_ent = {'type': tool, 'color': curr_color, 'start': start_pos, 'end': current_mouse}
            draw_shape(screen, temp_ent, width=1)

        pygame.display.flip()
        clock.tick(60)

def draw_shape(surface, ent, width=2):
    """Universal function to handle drawing different shapes based on type."""
    t = ent['type']
    color = ent['color']
    
    if t == 'brush':
        pygame.draw.circle(surface, color, ent['pos'], ent.get('radius', 15))
    
    elif t == 'rect':
        rect = get_rect(ent['start'], ent['end'])
        pygame.draw.rect(surface, color, rect, width)

    elif t == 'square':
        # To make a square, we use the smaller of the two distances (dx, dy)
        x1, y1 = ent['start']
        x2, y2 = ent['end']
        side = min(abs(x2 - x1), abs(y2 - y1))
        # Adjust direction based on mouse position
        sx = 1 if x2 > x1 else -1
        sy = 1 if y2 > y1 else -1
        sq_rect = pygame.Rect(x1, y1, side * sx, side * sy)
        sq_rect.normalize()
        pygame.draw.rect(surface, color, sq_rect, width)

    elif t == 'circle':
        # Calculate radius using distance formula
        rad = int(math.hypot(ent['start'][0] - ent['end'][0], ent['start'][1] - ent['end'][1]))
        pygame.draw.circle(surface, color, ent['start'], rad, width)

    elif t == 'right_tri':
        # Vertices: Click point, point directly below click, and current mouse X
        x1, y1 = ent['start']
        x2, y2 = ent['end']
        points = [(x1, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(surface, color, points, width)

    elif t == 'eq_tri':
        # Uses start_pos as top vertex, distance to end_pos as side length
        x1, y1 = ent['start']
        x2, y2 = ent['end']
        side = math.hypot(x2 - x1, y2 - y1)
        height = (math.sqrt(3) / 2) * side
        # Calculate base points relative to top
        points = [
            (x1, y1), 
            (x1 - side/2, y1 + height), 
            (x1 + side/2, y1 + height)
        ]
        pygame.draw.polygon(surface, color, points, width)

    elif t == 'rhombus':
        # Vertices at top, bottom, left, and right midpoints of the bounding box
        x1, y1 = ent['start']
        x2, y2 = ent['end']
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        points = [
            (mid_x, y1), # Top
            (x2, mid_y), # Right
            (mid_x, y2), # Bottom
            (x1, mid_y)  # Left
        ]
        pygame.draw.polygon(surface, color, points, width)

def get_rect(start, end):
    """Helper to calculate rect dimensions regardless of drag direction"""
    x1, y1 = start
    x2, y2 = end
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

if __name__ == "__main__":
    main()