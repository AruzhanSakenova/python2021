import pygame
import sys
from pygame.locals import *
import random
import time
from random import randint 
#import sleep
#import pygame as pg

#from pygame import mixer 
#mixer.init()
#mixer.music.load('crash.wav')
#mixer.music.play()
 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DOLL=0
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
DOLL=0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet2.bmp")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def get_speed(self):
          return random.randint(1,5)
    def __init__(self):
          super().__init__() 
          self.image = pygame.image.load('Enemy.bmp').convert()
          self.surf = pygame.Surface((42, 70))
          self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))
          self.speed = self.get_speed()
    def move(self):
        global SCORE
        self.rect.move_ip(0,self.speed)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.speed = self.get_speed() 

 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('dollar.bmp').convert()
        #self.image.set_colorkey(WHITE)
        self.surf = pygame.Surface((50,50))
        self.rect = self.image.get_rect()
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))

    
    def move(self):
        global DOLL
        self.rect.move_ip(0,5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            #DOLL+=1
    

    def coll(self):
        self.rect.move_ip(0,5)
        self.rect.top = 0
        self.rect.center = (500, 700)
            #DOLL+=1
    


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.bmp").convert_alpha()
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (160, 520))
        #self.image.set_colorkey(WHITE)
        #self.rect = self.image.get_rect()

        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins = pygame.sprite.Group()
coins.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(background , WHITE,(9, 10, 50, 45),) 
    pygame.draw.rect(background , WHITE,(345, 10, 50, 45),)  

    

    f2 = pygame.font.SysFont(None, 25)
    text2 = f2.render('score', False, BLACK)
    background.blit(text2, (10, 10))

    f1 = pygame.font.SysFont(None, 25)
    text2 = f2.render('coins', False, BLACK)
    background.blit(text2, (347, 10))

 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (23,22))
    scores1 = font_small.render(str(DOLL), True, BLACK)
    DISPLAYSURF.blit(scores1, (360,22))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, coins):
        DOLL+=1
        C1.coll()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          #pygame.mixer.Sound('crash.wav').play()
          #time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()
    
    #if pygame.sprite.spritecollideany(P1, coins):
     #   DOLL+=1
      #  C1.coll()
             
    pygame.display.update()
    FramePerSec.tick(FPS)