import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 500
# Задаем цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
running = True
red = 0
green = 0
blue = 0
while running:
    clock.tick(FPS)
    screen.fill((blue,green,red))
    green = green + 1
    blue - blue + 1

    if green == 255:
        green = 0
    if blue == 255:
        blue = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()