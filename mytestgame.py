import pygame, sys
from pygame.locals import *

#COLORS
BACKGROUND = (34,34,34)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRASS = (11, 102, 35)
SKY = (135, 206, 235)

#Initialize the pygame
pygame.init()

size = (960,640)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Test Game")

clock = pygame.time.Clock()

width = 30
height = 50 

x = 100
y = 559 - height

dx = 5
dy = 5

isJump = False
jumpCount = 10

def close():
    sys.exit()
    pygame.quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            close()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > dx: 
        x -= dx

    if keys[pygame.K_RIGHT] and x < 960 - dx - width:  
        x += dx
        
    if not(isJump): 
        #if keys[pygame.K_UP] and y > dy:
            #y -= dy

        #if keys[pygame.K_DOWN] and y < 640 - height - dy:
            #y += dy

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    screen.fill(SKY)
    #-------------------
    pygame.draw.rect(screen, RED, (x, y, width, height))

    pygame.draw.rect(screen, GRASS, (0,560,960,80))
    #-------------------
    pygame.display.flip()
    clock.tick(60)
