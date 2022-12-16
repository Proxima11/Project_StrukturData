import pygame
from StrukturData import Cave
from questions import question
import time

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Potats Miner")



#Struktur data
cave = Cave()
for i in range(8):
    cave.addRoomCave(i+1)
currentroom = cave.root

#tambah pertanyaan ke tiap ruangan
cave.addQuestion()

# menu variable 
menu = True
hover_play = False
hover_highscore = False
hover_exit = False

# game variables
play = False
locked = currentroom.locked
right = True
question = False
loading = False
door1 = False
door2 = False
door3 = False
change = False
startpause = 0

# menu images
menu_bg = pygame.image.load("menubg.png").convert_alpha()
menu_blank = pygame.image.load("menublank.png").convert_alpha()
menu_play = pygame.image.load("menuplay.png").convert_alpha()
menu_highscore = pygame.image.load("menuhighscore.png").convert_alpha()
menu_exit = pygame.image.load("menuexit.png").convert_alpha()
game_title = pygame.image.load("gametitle.png").convert_alpha()
menu_potato = pygame.image.load("menupotato.png").convert_alpha()

# game images
locked_bg = pygame.image.load("locked.png").convert_alpha()
double_door = pygame.image.load("double door.png").convert_alpha()
potato_right = pygame.image.load("potato.png").convert_alpha()
potato_left = pygame.image.load("potatoleft.png").convert_alpha()
notification = pygame.image.load("notification.png").convert_alpha()

# movement
potato_x = 350
potato_y = 450

def draw_menu():
    screen.blit(menu_bg, (0,0))
    screen.blit(game_title, (0,0))
    
    screen.blit(menu_potato, (0,0))

    if hover_play:
        screen.blit(menu_play(0,0))
    elif hover_highscore:
        screen.blit(menu_highscore(0,0))
    elif hover_exit:
        screen.blit(menu_exit(0,0))
    else : screen.blit(menu_blank, (0,0))

# draw game room
def draw_room():
    if locked:
        screen.blit(locked_bg, (0,0))
    else:
        screen.blit(double_door, (0,0))

def draw_potato():
    if right: screen.blit(potato_right, (potato_x , potato_y))
    else: screen.blit(potato_left, (potato_x, potato_y))

def draw_notification():
    if question: screen.blit(notification, (350, 250))
    if door1: screen.blit(notification, (250, 30))
    if door2: screen.blit(notification, (350, 20))
    if door3: screen.blit(notification, (550, 15))

run = True


#game play
while run:
    if menu:
        draw_menu()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_x>100 and mouse_x<200 and mouse_y > 100 and mouse_y < 200:
            hover_play = True
        else : hover_play = False

    clock.tick(FPS)
    if play:
        if not change:
            #gambar ruangan
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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        else:
            # 3 detik black screen pas mau ganti room
            if (startpause+3)<time.time():
                change = False
                locked = currentroom.locked
                if currentroom.left==None and currentroom.right==None:
                    double_door = pygame.image.load("room.png").convert_alpha()
                print('tree: level',currentroom.level)
            else:
                screen.fill((0,0,0))
    

    #kalau sudah sampai jalan kanan/kiri
    if (potato_x>=200 and potato_x<=300)and potato_y==160 and currentroom.left!=None:
        startpause= time.time()
        potato_x = 350
        potato_y = 450
        change = True
        if currentroom.left != None:
            currentroom = currentroom.left

    if (potato_x>=450 and potato_x<=550)and potato_y==160 and currentroom.right!=None:
        startpause= time.time()
        potato_x = 350
        potato_y = 450
        change = True
        currentroom = currentroom.right
        

        
    pygame.display.update()

pygame.quit()
