import pygame
import random

# Переменные с размером экрана
WIDTH = 1240
HEIGHT = 720

FPS = 999
# Задаем цвета
WHITE = (255,255,255)
BLACK = (255,255,255)
GREEN = (0,255,0)
RED = (0,0,255)
BLUE = (0,0,255)
# создаем игру и окно
pygame.init()
pygame.mixer.init()

# создаем переменную, в которую запихиваем экран, устонавливаем ширину и высоту
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# название игры
pygame.display.set_caption("My game")
# переменная, которая хранит время обновления экрана
clock = pygame.time.Clock()
# цикл игры
running = True
# цвет фона
screenColor = (0,0,0)

# параметры игрока
y = 0
x = 0
# ширина и высота игрока
width_player = 25
height_player = 25

# цвет яблока
colorApple = (255, 0, 50)
# координаты яблока
x_apple = 100
y_apple = 200

img = pygame.image.load("./Яблоко.png")


# rect = img.get_rect(center=(200,200))
# rect.center = WIDTH//2, HEIGHT//2

scale = pygame.transform.scale(img,(img.get_width()//12,img.get_height()//12))
scale_rect = scale.get_rect(center=(WIDTH//2,HEIGHT//2))

#dada
dada_img = pygame.image.load("./dada.png")
scale_dada = pygame.transform.scale(dada_img, (200,200))
dada_rect = scale_dada.get_rect()
dada_rect.center = 100,100

# screen.blit(scale,scale_rect)
# screen.blit(scale_dada,scale_rect)
# pygame.display.update()

# pygame.time.wait(5000)


#цикл
while running:
    #держим цикл на правильной скорости
    clock.tick(FPS)
    # заполнять экран цветом
    screen.fill(screenColor)
    screen.blit(scale,scale_rect)
    screen.blit(scale_dada,dada_rect)

    # рисуем прямоугольный прямоугольник который квадрат  с цветом координатами и размером
    pygame.draw.rect(screen,(100,90,200),[x,y,width_player,height_player])

    # рисуем яблоко 15 - это R радиус
    pygame.draw.circle(screen,colorApple,[x_apple,y_apple],10)


    if (x<0 or x > WIDTH - width_player):
        running = False
        pass
    #Столькновение с шариком
    if ((x < x_apple+15 and x_apple-15 < x + width_player) and (y < y_apple+15 and y_apple-15 < y + height_player)):
        width_player += 10
        x_apple = random.randint(0,WIDTH)
        y_apple = random.randint(0,HEIGHT)
        scale_rect.center = x_apple, y_apple
        pygame.draw.circle(screen,colorApple,[x_apple,y_apple],10)

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y = y - 2
    if keys[pygame.K_s]:
        y = y + 2
    if keys[pygame.K_a]:
        x = x - 2
    if keys[pygame.K_d]:
        x = x + 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()
pygame.quit()