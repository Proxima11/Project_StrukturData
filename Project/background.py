import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Potats Miner")

scroll = 0

bg_images = []
for i in range (1,6):
    bg_image = pygame.image.load(f"bg{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = 1920    

# variables
locked = True
right = True
question = False
door1 = False
door2 = False
door3 = False

# images
locked_bg = pygame.image.load("locked.png").convert_alpha()
double_door = pygame.image.load("double door.png").convert_alpha()
potato_right = pygame.image.load("potato.png").convert_alpha()
potato_left = pygame.image.load("potatoleft.png").convert_alpha()
notification = pygame.image.load("notification.png").convert_alpha()

# movement
potato_x = 350
potato_y = 450

def draw_room():
    if locked:
        screen.blit(locked_bg, (0,0))
    else:
        screen.blit(double_door, (0,0))

def draw_potato():
    if right: screen.blit(potato_right, (potato_x , potato_y))
    else: screen.blit(potato_left, (potato_x, potato_y))

def draw_bg():
    for x in range(5):
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
            speed += 0.2

def draw_notification():
    if question: screen.blit(notification, (350, 250))
    if door1: screen.blit(notification, (250, 30))
    if door2: screen.blit(notification, (350, 20))
    if door3: screen.blit(notification, (550, 15))

run = True
while run:

    clock.tick(FPS)

    # gambar ruangan
    draw_room()

    # gambar potato
    draw_potato()
    move = pygame.key.get_pressed()
    if potato_y > 300:
        if move[pygame.K_LEFT]:
            if potato_x > 100: potato_x-=5
            right = False
        if move[pygame.K_RIGHT]:
            if potato_x < 650: potato_x+=5
            right = True
        if move[pygame.K_UP]:
            if locked:
                if potato_y > 370: potato_y-=5
            else:    
                potato_y-=5
        if move[pygame.K_DOWN]:
            if potato_y < 450: potato_y+=5
    elif potato_y > 160:
        if move[pygame.K_LEFT]:
            if potato_x > 170: potato_x-=5
            right = False
        if move[pygame.K_RIGHT]:
            if potato_x < 680: potato_x+=5
            right = True
        if move[pygame.K_UP]:
            if potato_x > 180 and potato_x < 630: potato_y-=5
        if move[pygame.K_DOWN]:
            if potato_x > 160 and potato_x < 670 : potato_y+=5
    else:
        if move[pygame.K_LEFT]:
            if potato_x > 230: potato_x-=5
            right = False
        if move[pygame.K_RIGHT]:
            if potato_x < 550: potato_x+=5
            right = True
        if move[pygame.K_DOWN]:
            if potato_x > 220 and potato_x < 550: potato_y+=5

    # notifikasi
    draw_notification()
    if ((potato_x > 250 and potato_x < 500) and (potato_y < 400 and potato_y > 350)) and locked is not False: 
        question = True
        key = pygame.key.get_pressed()
        if key[pygame.K_e]:
            locked = False
    else : question = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    if key[pygame.K_RIGHT] and scroll < 3000:
        scroll += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
