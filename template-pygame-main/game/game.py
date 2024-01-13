import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 500
# Задаем цвета
WHITE = (255,255,255)
BLACK = (255,255,255)
GREEN = (0,255,0)
RED = (0,0,255)
BLUE = (0,0,255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
running = True
red = 0
green = 0
black = 0
blue = 0
isRedMax = False

y= 0

while running:
    clock.tick(FPS)
    screen.fill((red,green,blue))
    if isRedMax == True:
        green = green + 0.5
    else:
        red = red + 0.5
        if red == 255:
            red = 0
            isRedMax = True
        print(red)
    pygame.draw.rect(screen,(100,50,200),[0,0,100,100])
    y = y + 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()