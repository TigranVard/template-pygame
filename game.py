import pygame
import random

WIDTH = 500
HEIGHT = 500
FPS = 500
# # Задаем цвета
# WHITE = (255,255,255)
# BLACK = (255,255,255)
# GREEN = (0,255,0)
# RED = (0,0,255)
# BLUE = (0,0,255)
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

y = 0
x = 0

colorApple = (255, 0, 50)
x_apple = 100
y_apple = 200

while running:
    clock.tick(FPS)
    screen.fill((red,green,blue))

    # if isRedMax == True:
    #     green = green + 0.5
    # else:
    #     red = red + 0.5
    #     if red == 255:
    #         red = 0
    #         isRedMax = True
    #     print(red)


    pygame.draw.rect(screen,(100,90,200),[x,y,20,20])
    #рисуем яблоко
    pygame.draw.circle(screen,colorApple,[x_apple,y_apple],20)

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y = y - 5
                print("Нажали на W")
            if event.key == pygame.K_s:
                y = y + 5
                print("Нажали на S")
            if event.key == pygame.K_a:
                x = x - 5
                print("Нажали на A")
            if event.key == pygame.K_d:
                x = x + 5
                print("Нажали на D")
            if event.key == pygame.K_SPACE:
                print("Нажали на SPACE")
        

        
    
    pygame.display.flip()
pygame.quit()