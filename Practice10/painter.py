import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Paint: [B]rush, [R]ect, [C]ircle, [E]raser | Colors: R, G, B, Y, W")
    clock = pygame.time.Clock()
    
    radius = 15
    drawing = False
    tool = 'brush' # Options: 'brush', 'rect', 'circle'
    curr_color = (0, 0, 255) # Default Blue
    
    # Store objects as: {'type': 'brush', 'color': (r,g,b), 'pos': (x,y), 'radius': r}
    # For shapes: {'type': 'rect', 'color': (r,g,b), 'start': (x,y), 'end': (x,y)}
    elements = []
    start_pos = None

    while True:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                # Tool Selection
                if event.key == pygame.K_b: tool = 'brush'
                if event.key == pygame.K_r: tool = 'rect'
                if event.key == pygame.K_c: tool = 'circle'
                if event.key == pygame.K_e: 
                    tool = 'brush'
                    curr_color = (0, 0, 0) # Eraser is just black brush
                
                # Color Selection
                if event.key == pygame.K_1: curr_color = (255, 0, 0) # Red
                if event.key == pygame.K_2: curr_color = (0, 255, 0) # Green
                if event.key == pygame.K_3: curr_color = (0, 0, 255) # Blue
                if event.key == pygame.K_4: curr_color = (255, 255, 0) # Yellow
                if event.key == pygame.K_5: curr_color = (255, 255, 255) # White
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                if tool == 'brush':
                    elements.append({'type': 'brush', 'color': curr_color, 'pos': event.pos, 'radius': radius})

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing and tool in ['rect', 'circle']:
                    elements.append({'type': tool, 'color': curr_color, 'start': start_pos, 'end': event.pos, 'radius': radius})
                drawing = False

            if event.type == pygame.MOUSEMOTION:
                if drawing and tool == 'brush':
                    elements.append({'type': 'brush', 'color': curr_color, 'pos': event.pos, 'radius': radius})

        # Draw all stored elements
        for ent in elements:
            if ent['type'] == 'brush':
                pygame.draw.circle(screen, ent['color'], ent['pos'], ent['radius'])
            elif ent['type'] == 'rect':
                r_rect = get_rect(ent['start'], ent['end'])
                pygame.draw.rect(screen, ent['color'], r_rect, 2)
            elif ent['type'] == 'circle':
                r_rad = int(((ent['start'][0]-ent['end'][0])**2 + (ent['start'][1]-ent['end'][1])**2)**0.5)
                pygame.draw.circle(screen, ent['color'], ent['start'], r_rad, 2)

        # Draw visual feedback for shape being dragged
        if drawing and tool in ['rect', 'circle']:
            current_mouse = pygame.mouse.get_pos()
            if tool == 'rect':
                pygame.draw.rect(screen, curr_color, get_rect(start_pos, current_mouse), 1)
            else:
                temp_rad = int(((start_pos[0]-current_mouse[0])**2 + (start_pos[1]-current_mouse[1])**2)**0.5)
                pygame.draw.circle(screen, curr_color, start_pos, temp_rad, 1)

        pygame.display.flip()
        clock.tick(60)

def get_rect(start, end):
    """Helper to calculate rect dimensions regardless of drag direction"""
    x1, y1 = start
    x2, y2 = end
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

if __name__ == "__main__":
    main()