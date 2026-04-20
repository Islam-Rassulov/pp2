import pygame
import random
import sys

# --- Configuration & Constants ---
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS_START = 10  # Initial speed

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY  = (50, 50, 50)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake: Level Up Edition")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.reset_game()

    def reset_game(self):
        """Initializes or restarts the game state."""
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = (GRID_SIZE, 0)
        self.score = 0
        self.level = 1
        self.speed = FPS_START
        self.food = self.generate_food()
        self.game_over = False

    def generate_food(self):
        """Generates food at a random position not occupied by the snake or walls."""
        while True:
            # Generate random coordinates aligned with the grid
            x = random.randrange(0, WIDTH, GRID_SIZE)
            y = random.randrange(0, HEIGHT, GRID_SIZE)
            pos = (x, y)
            
            # Ensure food doesn't spawn inside the snake body
            if pos not in self.snake:
                return pos

    def update(self):
        """Handles movement, collisions, and level logic."""
        if self.game_over:
            return

        # 1. Calculate new head position
        new_head = (self.snake[0][0] + self.direction[0], 
                    self.snake[0][1] + self.direction[1])

        # 2. Border Collision: Check if head leaves the playing area
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return

        # 3. Self Collision: Check if snake hits itself
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # 4. Food Collection
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
            
            # 5. Level Up Logic: Every 3 food items
            if self.score % 3 == 0:
                self.level += 1
                self.speed += 2  # Increase difficulty by increasing FPS
        else:
            # Remove tail if no food eaten
            self.snake.pop()

    def draw(self):
        """Renders everything to the screen."""
        self.screen.fill(BLACK)

        # Draw Snake
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, (*segment, GRID_SIZE - 2, GRID_SIZE - 2))

        # Draw Food
        pygame.draw.rect(self.screen, RED, (*self.food, GRID_SIZE - 2, GRID_SIZE - 2))

        # Draw UI (Score and Level)
        score_text = self.font.render(f"Score: {self.score}  Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            msg = self.font.render("GAME OVER! Press R to Restart", True, WHITE)
            self.screen.blit(msg, (WIDTH // 4, HEIGHT // 2))

        pygame.display.flip()

    def run(self):
        """Main game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Input Handling
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