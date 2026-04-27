import pygame
import random
import sys

# --- Configuration & Constants ---
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS_START = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

# Food configurations: Weight determines spawn chance
FOOD_TYPES = {
    "APPLE": {"color": RED, "weight": 70, "points": 1, "lifespan": 5000},    # Common, lasts 5s
    "GOLDEN": {"color": GOLD, "weight": 30, "points": 5, "lifespan": 2000}  # Rare, lasts 2s
}

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake: Level Up Edition")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.reset_game()

    def reset_game(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = (GRID_SIZE, 0)
        self.score = 0
        self.level = 1
        self.speed = FPS_START
        self.food = self.generate_food()
        self.game_over = False

    def generate_food(self):
        """Generates food using weighted probabilities."""
        while True:
            x = random.randrange(0, WIDTH, GRID_SIZE)
            y = random.randrange(0, HEIGHT, GRID_SIZE)
            pos = (x, y)
            
            if pos not in self.snake:
                # Weighted selection: extract keys and weights
                food_keys = list(FOOD_TYPES.keys())
                weights = [f['weight'] for f in FOOD_TYPES.values()]
                
                # Pick a food type based on weights
                selected_type = random.choices(food_keys, weights=weights, k=1)[0]
                
                # Return dictionary with metadata
                return {
                    "pos": pos,
                    "type": selected_type,
                    "config": FOOD_TYPES[selected_type],
                    "spawn_time": pygame.time.get_ticks()
                }

    def update(self):
        if self.game_over:
            return

        # --- Handle Timed Food Decay ---
        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.food['spawn_time']
        
        # If food lifespan is exceeded, respawn it
        if elapsed > self.food['config']['lifespan']:
            self.food = self.generate_food()

        # 1. Calculate new head position
        new_head = (self.snake[0][0] + self.direction[0], 
                    self.snake[0][1] + self.direction[1])

        # 2. Border Collision
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return

        # 3. Self Collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # 4. Food Collection
        if new_head == self.food['pos']:
            self.score += self.food['config']['points']
            self.food = self.generate_food()
            
            # 5. Level Up Logic
            if self.score % 5 == 0: # Adjusted scaling slightly
                self.level += 1
                self.speed += 1
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill(BLACK)

        # Draw Snake
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, (*segment, GRID_SIZE - 2, GRID_SIZE - 2))

        # Draw Food (Using specific color from config)
        food_cfg = self.food['config']
        pygame.draw.rect(self.screen, food_cfg['color'], (*self.food['pos'], GRID_SIZE - 2, GRID_SIZE - 2))

        # Draw UI
        score_text = self.font.render(f"Score: {self.score}  Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            msg = self.font.render("GAME OVER! Press R to Restart", True, WHITE)
            self.screen.blit(msg, (WIDTH // 4, HEIGHT // 2))

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if self.game_over and event.key == pygame.K_r:
                        self.reset_game()
                    elif event.key == pygame.K_UP and self.direction != (0, GRID_SIZE):
                        self.direction = (0, -GRID_SIZE)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -GRID_SIZE):
                        self.direction = (0, GRID_SIZE)
                    elif event.key == pygame.K_LEFT and self.direction != (GRID_SIZE, 0):
                        self.direction = (-GRID_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-GRID_SIZE, 0):
                        self.direction = (GRID_SIZE, 0)

            self.update()
            self.draw()
            self.clock.tick(self.speed)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()