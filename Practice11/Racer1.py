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

# Other Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0 
N = 5 # Increase enemy speed every N coins collected

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
        self.raw_image = pygame.image.load("coin1.png")
        self.weight = 1 # Default weight
        self.reset()

    def reset(self):
        """Resets coin position and randomly assigns a weight/size"""
        # TASK: Randomly generating coins with different weights
        # 20% chance for a 'Gold' coin (Weight 3), 80% for 'Silver' (Weight 1)
        if random.random() > 0.8:
            self.weight = 3
            self.coin_size = (40, 40) # Slightly larger
        else:
            self.weight = 1
            self.coin_size = (25, 25)

        self.image = pygame.transform.scale(self.raw_image, self.coin_size)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        
        # Hitbox for collision accuracy
        self.hitbox = pygame.Rect(0, 0, self.coin_size[0] * 0.8, self.coin_size[1] * 0.8)
        self.hitbox.center = self.rect.center

    def move(self):
        self.rect.move_ip(0, SPEED)
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
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Setting up Sprites         
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Timer to increase speed automatically over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2 # Slower natural speed increase
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coin_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Custom Collision for Coins
    for coin in coins:
        if P1.rect.colliderect(coin.hitbox):
            # Update score by the specific coin's weight
            COIN_SCORE += coin.weight
            
            # TASK: Increase speed of Enemy when player earns N coins
            if COIN_SCORE % N == 0:
                SPEED += 1.0 # Significant speed boost
                
            coin.reset() 

    # Collision Detection: Player vs Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()         
        
    pygame.display.update()
    FramePerSec.tick(FPS)