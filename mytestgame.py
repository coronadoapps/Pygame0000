import pygame, sys, random
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
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
size = (WINDOW_WIDTH,WINDOW_HEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

width = 50
height = 50 

x = WINDOW_WIDTH/2
y = WINDOW_HEIGHT/2

dx = 7
dy = 7

isJump = False
jumpCount = 10

def close():
    pygame.quit()
    sys.exit()
    

def drawGrid():
    blockSize = 80 #Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

def drawFood():
    random_color = (random.uniform(0,255), random.uniform(0,255), random.uniform(0,255))
    random_pos = (random.uniform(0,WINDOW_WIDTH), random.uniform(0,WINDOW_HEIGHT))

    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            pygame.draw.circle(screen, random_color, random_pos, 10)


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
        if keys[pygame.K_UP] and y > dy:
            y -= dy

        if keys[pygame.K_DOWN] and y < 640 - height - dy:
            y += dy

        #if keys[pygame.K_SPACE]:
            #isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    screen.fill(BACKGROUND)
    #-------------------
    pygame.draw.rect(screen, WHITE, (x, y, width, height))
    #-------------------
    pygame.display.update()
    clock.tick(60)


