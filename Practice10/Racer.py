import pygame, sys
from pygame.locals import *
import random, time

# Initializing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0 

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the generated coin image
        self.raw_image = pygame.image.load("coin1.png")
        
        # --- CHANGE 1: Define specific size for the coin (smaller than a car) ---
        self.coin_size = (30, 30) # Example: 30x30 pixels
        # Scale the image down to this size
        self.image = pygame.transform.scale(self.raw_image, self.coin_size)
        
        self.rect = self.image.get_rect()
        
        # --- CHANGE 2: Define a smaller collision hit box ---
        # We use a separate pygame.Rect for collisions, slightly smaller than the image
        self.hitbox = pygame.Rect(0, 0, self.coin_size[0] * 0.7, self.coin_size[1] * 0.7)
        
        self.reset()

    def reset(self):
        """Resets the coin to the top of the screen"""
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        # Keep the hitbox aligned with the image center
        self.hitbox.center = self.rect.center

    def move(self):
        self.rect.move_ip(0, SPEED)
        # Always update hitbox position when rect moves
        self.hitbox.center = self.rect.center
        
        if (self.rect.bottom > 600):
            self.reset()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event to increase speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw Background
    DISPLAYSURF.blit(background, (0, 0))
    
    # Render and display Score (Left) and Coin Count (Right)
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coin_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # --- CHANGE 3: Custom Collision Detection (Player vs Coin Hitbox) ---
    # spritecollideany uses rects. We must manually check the player rect
    # against the specific coin hitbox.
    
    # Check collison against the 'coins' group, but using the hitbox
    for coin in coins:
        if P1.rect.colliderect(coin.hitbox):
            COIN_SCORE += 1
            coin.reset() # Move coin back to top immediately

    # Collision Detection: Player vs Enemy (uses default rects)
    if pygame.sprite.spritecollideany(P1, enemies):
        # Ensure 'crash.wav' exists or comment this line out
        # pygame.mixer.Sound('crash.wav').play() 
        time.sleep(1)
        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)