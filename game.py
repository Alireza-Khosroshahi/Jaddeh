import pygame
import random
from pygame import mixer
pygame.init()

# main screen 
screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Jaddeh")
icon = pygame.image.load('icon.png')
backgroundimg = pygame.image.load('background.png')
#player
playerimg = pygame.image.load('player.png')
player_x=200
player_y=500
player_movment=0
pmp=4
health = 3
#musica
background_sound=mixer.Sound('race_back_music.mp3')
background_sound.play(-1)
car_sound = mixer.Sound('car_sound.mp3')
#health
health_img_1 = pygame.image.load('health 1.png')
health_img_2 = pygame.image.load('health 2.png')
health_img_3 = pygame.image.load('health 3.png')
#car
car_number=3 #at most 4
car_img = []
car_x = []
car_y = []
for i in range(car_number):
    cartype= random.randint(1,6)
    if cartype ==1:
        car_img.append(pygame.image.load('car1.png'))
    if cartype ==2:
        car_img.append(pygame.image.load('car2.png'))
    if cartype ==3:
        car_img.append(pygame.image.load('car3.png'))
    if cartype ==4:
        car_img.append(pygame.image.load('car4.png'))
    if cartype ==5:
        car_img.append(pygame.image.load('car5.png'))
    if cartype ==6:
        car_img.append(pygame.image.load('car6.png'))
    car_position=random.randint(1,4)
    if car_position == 1:
        car_x.append(280)
    if car_position == 2:
        car_x.append(456)
    if car_position == 3:
        car_x.append(646)
    if car_position == 4:
        car_x.append(828)
    car_y.append(-100)
cym=5
bcym=3
car_y_movment=bcym
pygame.display.set_icon(icon)
running = True
def player(x,y):
    screen.blit(playerimg,(x,y))
def car(x,y,i):
    screen.blit(car_img[i],(x,y))
def collison(x1,y1,x2,y2):
    car_rect= pygame.Rect(x1,y1,90,154)
    player_rect= pygame.Rect(x2,y2,100,189)
    if player_rect.colliderect(car_rect):
        return True
    else:
        return False
    
def health_show(i):
    if i == 1:
        screen.blit(health_img_1,(5,5))
    if i == 2:
        screen.blit(health_img_2,(5,5))
    if i == 3:
        screen.blit(health_img_3,(5,5))

while running:
    screen.blit(backgroundimg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_movment= pmp
            if event.key == pygame.K_a:
                player_movment= -pmp
            if event.key == pygame.K_w:
                car_y_movment = cym
                car_sound.play()
                car_sound.set_volume(100)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_movment= 0
            if event.key == pygame.K_a:
                player_movment= 0
            if event.key == pygame.K_w:
                car_y_movment = bcym
                car_sound.set_volume(0)
            
    player_x += player_movment
    if player_x < 244:
        player_x = 244
    elif player_x > 860:
        player_x =860
    
    for i in range(car_number):
        if car_y[i] > 700:
            car_position=random.randint(1,4)
            if car_position == 1:
                car_x[i]=280
            if car_position == 2:
                car_x[i]=456
            if car_position == 3:
                car_x[i]=646
            if car_position == 4:
                car_x[i]=828
            car_y[i]=-50    
    for i in range(car_number):
        car_y[i] += car_y_movment
    player(player_x,player_y)
    for i in range(car_number):
        collison_state = collison(car_x[i],car_y[i],player_x,player_y)
        if collison_state :
            car_y[i] = 701
            health -=1
            cartype= random.randint(1,6)
            if cartype ==1:
                car_img[i] = pygame.image.load('car1.png')
            if cartype ==2:
                car_img[i] = pygame.image.load('car2.png')
            if cartype ==3:
                car_img[i] = pygame.image.load('car3.png')
            if cartype ==4:
                car_img[i] = pygame.image.load('car4.png')
            if cartype ==5:
                car_img[i] = pygame.image.load('car5.png')
            if cartype ==6:
                car_img[i] = pygame.image.load('car6.png')
    health_show(health)
    if health == 0:
       running = False 
    for i in range(car_number):
        car(car_x[i],car_y[i],i)
    pygame.display.update()