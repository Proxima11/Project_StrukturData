import pygame
from StrukturData import Cave
from questions import question
import time
import queue as q


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
mainroom = cave.root

#tambah pertanyaan ke tiap ruangan
cave.addQuestion()
cave.printRoom()

#tambah powerup
cave.addPowerUp()
# queue untuk power up nantinya
# queue = q.SimpleQueue()
# queue.put(0)
# queue.put(0)

queue = [1,3]

# menu variable 
menu = True
hover_play = False
hover_highscore = False
hover_exit = False

# game variables
play = False
paused = False
locked = currentroom.locked
right = True
question_notif = False
loading = False
door1 = False
door2 = False
door3 = False
change = False
startpause = 0
powerupdelay = 0
isdelay = False
leftdoor = False
rightdoor = False
questionpage = False

# menu images
menu_bg = pygame.image.load("menubg.png").convert_alpha()
menu_blank = pygame.image.load("menublank.png").convert_alpha()
menu_play = pygame.image.load("menuplay.png").convert_alpha()
menu_highscore = pygame.image.load("menuhighscore.png").convert_alpha()
menu_exit = pygame.image.load("menuexit.png").convert_alpha()
game_title = pygame.image.load("gametitle.png").convert_alpha()
menu_potato = pygame.image.load("menupotato.png").convert_alpha()

# game images
main_room_double = pygame.image.load("main room double.png").convert_alpha()
main_room_left = pygame.image.load("main room left.png").convert_alpha()
main_room_right = pygame.image.load("main room right.png").convert_alpha()
locked_bg = pygame.image.load("locked.png").convert_alpha()
double_door = pygame.image.load("double door.png").convert_alpha()
left_door = pygame.image.load("door left.png").convert_alpha()
right_door = pygame.image.load("door right.png").convert_alpha()
no_door = pygame.image.load("dead end.png").convert_alpha()
potato_right = pygame.image.load("potato.png").convert_alpha()
potato_left = pygame.image.load("potatoleft.png").convert_alpha()
notification = pygame.image.load("notification.png").convert_alpha()
treasure = pygame.image.load("treasure.png").convert_alpha()

# power up images
powerUptime = pygame.image.load("powerupbonustime.png").convert_alpha()
powerUproot = pygame.image.load("powerupcheckroot.png").convert_alpha()
powerUplevel = pygame.image.load("powerupshowlevel.png").convert_alpha()
powerUphint = pygame.image.load("powerupquestionhint.png").convert_alpha()

powerup1empty = pygame.image.load("powerup1empty.png").convert_alpha()
powerup1time = pygame.image.load("powerup1time.png").convert_alpha()
powerup1root = pygame.image.load("powerup1root.png").convert_alpha()
powerup1level = pygame.image.load("powerup1level.png").convert_alpha()
powerup1hint = pygame.image.load("powerup1hint.png").convert_alpha()

powerup2empty = pygame.image.load("powerup2empty.png").convert_alpha()
powerup2time = pygame.image.load("powerup2time.png").convert_alpha()
powerup2root = pygame.image.load("powerup2root.png").convert_alpha()
powerup2level = pygame.image.load("powerup2level.png").convert_alpha()
powerup2hint = pygame.image.load("powerup2hint.png").convert_alpha()

# question images
questionbg = pygame.image.load("questionbg.png").convert_alpha()
choice1 = pygame.image.load("choice1.png").convert_alpha()
choice2 = pygame.image.load("choice2.png").convert_alpha()
choice3 = pygame.image.load("choice3.png").convert_alpha()
choice4 = pygame.image.load("choice4.png").convert_alpha()

# movement
potato_x = 350
potato_y = 450
mouse_x = 0
mouse_y = 0

def draw_menu():
    screen.blit(menu_bg, (0,0))
    screen.blit(game_title, (0,0))
    screen.blit(menu_potato, (0,0))

    if hover_play:
        screen.blit(menu_play, (0,0))
    elif hover_highscore:
        screen.blit(menu_highscore, (0,0))
    elif hover_exit:
        screen.blit(menu_exit, (0,0))
    else : screen.blit(menu_blank, (0,0))

# draw game room
def draw_room():
    if locked:
        screen.blit(locked_bg, (0,0))
    else:
        if currentroom == mainroom:
            if rightdoor and leftdoor:
                screen.blit(main_room_double, (0,0))
            elif rightdoor and not leftdoor:
                screen.blit(main_room_right, (0,0))
            elif leftdoor and not rightdoor:
                screen.blit(main_room_left, (0,0))
        else:
            if rightdoor and leftdoor:
                screen.blit(double_door, (0,0))
            elif rightdoor and not leftdoor:
                screen.blit(right_door, (0,0))
            elif leftdoor and not rightdoor:
                screen.blit(left_door, (0,0))
            else: screen.blit(no_door, (0,0))

def draw_potato():
    if right: screen.blit(potato_right, (potato_x , potato_y))
    else: screen.blit(potato_left, (potato_x, potato_y))

def draw_notification():
    if question_notif: screen.blit(notification, (350, 250))
    if door1: screen.blit(notification, (250, 30))
    if door2: screen.blit(notification, (350, 20))
    if door3: screen.blit(notification, (550, 15))

def draw_treasure():
    if currentroom.treasure and not locked:
        screen.blit(treasure, (0,0))

def draw_powerup():
    if currentroom.powerUp:
        if currentroom.powerUptype == 1:
            screen.blit(powerUptime, (0, 0))
        elif currentroom.powerUptype == 2:
            screen.blit(powerUproot, (0, 0))
        elif currentroom.powerUptype == 3:
            screen.blit(powerUplevel, (0, 0))
        elif currentroom.powerUptype == 4:
            screen.blit(powerUphint, (0, 0))

def draw_held_powerup():
    # powerup1 = queue.get()
    # powerup2 = queue.get()
    powerup1 = queue[0]
    powerup2 = queue[1]

    if powerup1 == 0:
        screen.blit(powerup1empty, (0, 0))
    elif powerup1 == 1:
        screen.blit(powerup1time, (0, 0))
    elif powerup1 == 2:
        screen.blit(powerup1root, (0, 0))
    elif powerup1 == 3:
        screen.blit(powerup1level, (0, 0))
    elif powerup1 == 4:
        screen.blit(powerup1hint, (0, 0))

    if powerup2 == 0:
        screen.blit(powerup2empty, (0, 0))
    elif powerup2 == 1:
        screen.blit(powerup2time, (0, 0))
    elif powerup2 == 2:
        screen.blit(powerup2root, (0, 0))
    elif powerup2 == 3:
        screen.blit(powerup2level, (0, 0))
    elif powerup2 == 4:
        screen.blit(powerup2hint, (0, 0))

    # queue.put(powerup1)
    # queue.put(powerup2)

def usePowerUp():
    use = queue.pop(0)
    if use == 0:
        print("no powerup")
        pass
    elif use == 1:
        pass
    elif use == 2:
        found = cave.poweruproot(currentroom)
        if found:
            pass
        else :
            pass
    elif use == 3:
        level = cave.poweruplevel()
        pass
    elif use == 4:
        pass
    queue.append(0)
    
# buat ngambil powerupnya pencet E
def getpowerup():
    if queue[0]==0 and queue[1]==0:
        queue[0]=currentroom.powerUptype
    elif queue[1]==0:
        queue[1]=currentroom.powerUptype
    else:
        queue.pop(0)
        queue.append(currentroom.powerUptype)
    currentroom.powerUp=False
    currentroom.powerUptype=0

def draw_question_():
    if currentroom.Question is not None and not currentroom.Question.isAnswered:
        white = (255, 255, 255)
        font = pygame.font.SysFont('freesansbold.ttf',28)
        collection = [word.split('/') for word in currentroom.Question.question.splitlines()]
        space = font.size(' ')[0]
        pos = (115,75)
        temp_x = pos[0]
        temp_y = pos[1]
        for lines in collection:
            for word in lines:
                word_surface = font.render(word, True, white)
                word_width, word_height = word_surface.get_size()
                if (temp_x + word_width) > 700:
                    temp_x=pos[0]
                    temp_y += 30
                screen.blit(word_surface, (temp_x,temp_y))
                temp_x += (word_width + space)
            temp_x = pos[0]
            temp_y = temp_y + 30
        temp_y += 30

def draw_answer1():
    if currentroom.Question is not None and not currentroom.Question.isAnswered:
        white = (255, 255, 255)
        font = pygame.font.SysFont('freesansbold.ttf',22)
        collection = [word.split('/') for word in currentroom.Question.answer[0].splitlines()]
        space = font.size(' ')[0]
        pos = (125,315)
        temp_x = pos[0]
        temp_y = pos[1]
        for lines in collection:
            for word in lines:
                word_surface = font.render(word, True, white)
                word_width, word_height = word_surface.get_size()
                if (temp_x + word_width) > 700:
                    temp_x=pos[0]
                    temp_y += 24
                screen.blit(word_surface, (temp_x,temp_y))
                temp_x += (word_width + space)
            temp_x = pos[0]
            temp_y = temp_y + 24

def draw_answer2():
    if currentroom.Question is not None and not currentroom.Question.isAnswered:
        white = (255, 255, 255)
        font = pygame.font.SysFont('freesansbold.ttf',22)
        collection = [word.split('/') for word in currentroom.Question.answer[1].splitlines()]
        space = font.size(' ')[0]
        pos = (520,315)
        temp_x = pos[0]
        temp_y = pos[1]
        for lines in collection:
            for word in lines:
                word_surface = font.render(word, True, white)
                word_width, word_height = word_surface.get_size()
                if (temp_x + word_width) > 700:
                    temp_x=pos[0]
                    temp_y += 24
                screen.blit(word_surface, (temp_x,temp_y))
                temp_x += (word_width + space)
            temp_x = pos[0]
            temp_y = temp_y + 24

def draw_answer3():
    if currentroom.Question is not None and not currentroom.Question.isAnswered and len(currentroom.Question.answer) > 2:
        white = (255, 255, 255)
        font = pygame.font.SysFont('freesansbold.ttf',22)
        collection = [word.split('/') for word in currentroom.Question.answer[2].splitlines()]
        space = font.size(' ')[0]
        pos = (125,460)
        temp_x = pos[0]
        temp_y = pos[1]
        for lines in collection:
            for word in lines:
                word_surface = font.render(word, True, white)
                word_width, word_height = word_surface.get_size()
                if (temp_x + word_width) > 700:
                    temp_x=pos[0]
                    temp_y += 24
                screen.blit(word_surface, (temp_x,temp_y))
                temp_x += (word_width + space)
            temp_x = pos[0]
            temp_y = temp_y + 24

def draw_answer4():
    if currentroom.Question is not None and not currentroom.Question.isAnswered  and len(currentroom.Question.answer) > 2:
        white = (255, 255, 255)
        font = pygame.font.SysFont('freesansbold.ttf', 22)
        collection = [word.split('/') for word in currentroom.Question.answer[3].splitlines()]
        space = font.size(' ')[0]
        pos = (520,460)
        temp_x = pos[0]
        temp_y = pos[1]
        for lines in collection:
            for word in lines:
                word_surface = font.render(word, True, white)
                word_width, word_height = word_surface.get_size()
                if (temp_x + word_width) > 700:
                    temp_x=pos[0]
                    temp_y += 24
                screen.blit(word_surface, (temp_x,temp_y))
                temp_x += (word_width + space)
            temp_x = pos[0]
            temp_y = temp_y + 24

def draw_question():
    screen.blit(questionbg,(0,0))
    screen.blit(choice1,(0,0))
    screen.blit(choice2,(0,0))
    screen.blit(choice3,(0,0))
    screen.blit(choice4,(0,0))
    draw_question_()
    draw_answer1()
    draw_answer2()
    draw_answer3()
    draw_answer4()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x > 115 and mouse_x < 350 and mouse_y > 255 and mouse_y < 390:
        click = pygame.mouse.get_pressed()
        if click[0]:
            currentroom.Question.isAnswered = True
            currentroom.Question.isCorrect(currentroom.Question.answer[0])
            currentroom.locked = False
    #235
    if mouse_x > 415 and mouse_x < 750 and mouse_y > 255 and mouse_y < 390:
        click = pygame.mouse.get_pressed()
        if click[0]:
            currentroom.Question.isAnswered = True
            currentroom.Question.isCorrect(currentroom.Question.answer[1])
            currentroom.locked = False
    #135
    if mouse_x > 115 and mouse_x < 350 and mouse_y > 415 and mouse_y < 550:
        click = pygame.mouse.get_pressed()
        if click[0]:
            currentroom.Question.isAnswered = True
            currentroom.Question.isCorrect(currentroom.Question.answer[2])
            currentroom.locked = False
    
    if mouse_x > 415 and mouse_x < 750 and mouse_y > 415 and mouse_y < 550:
        click = pygame.mouse.get_pressed()
        if click[0]:
            currentroom.Question.isAnswered = True
            currentroom.Question.isCorrect(currentroom.Question.answer[3])
            currentroom.locked = False
    pass

run = True

#game play
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    clock.tick(FPS)
    
    if menu:
        draw_menu()
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_x>520 and mouse_x<680 and mouse_y > 200 and mouse_y < 280:
            hover_play = True
            click = pygame.mouse.get_pressed()
            if click[0]: 
                menu = False
                play = True
        else : hover_play = False

        if mouse_x>500 and mouse_x<650 and mouse_y > 290 and mouse_y < 350:
            hover_highscore = True
            click = pygame.mouse.get_pressed()
            if click[0]: pass
        else : hover_highscore = False

        if mouse_x>500 and mouse_x<650 and mouse_y > 380 and mouse_y < 450:
            hover_exit = True
            click = pygame.mouse.get_pressed()
            if click[0]: run = False
        else : hover_exit = False

    elif play:
        if not change:


            # menentukan bentuk ruangan
            if currentroom.left != None:
                leftdoor = True
            else: leftdoor = False
            if currentroom.right != None:
                rightdoor = True
            else: rightdoor = False

            # status locked
            locked = currentroom.locked

            #gambar ruangan
            draw_room()

            # gambar powerup
            if not locked:
                draw_powerup()

            # gambar potato
            draw_potato()

            # gambar treasure
            draw_treasure()

            # gambar help powerup
            draw_held_powerup()

            usePU = pygame.key.get_pressed()
            if usePU[pygame.K_p] and powerupdelay+3<time.time(): #di kasih delay biar gak kepake e cuma 1 dalam 3 detik
                powerupdelay = time.time()
                usePowerUp()
                

            move = pygame.key.get_pressed()
            if potato_y >= 450 and currentroom != mainroom:
                if move[pygame.K_DOWN]:
                    if potato_x > 300 and potato_x < 500: potato_y+=5
                if move[pygame.K_LEFT]:
                    if potato_x > 200 and potato_x < 400 and potato_y > 500: potato_x+=5
                    else: potato_x = potato_x
                if move[pygame.K_RIGHT]:
                    if potato_x < 400 and potato_x > 200 and potato_y > 500: potato_x-=5
                    else : potato_x = potato_x
                if move[pygame.K_UP]:
                    if potato_x > 300 and potato_x < 500: potato_y-=5
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
                question_notif = True
                key = pygame.key.get_pressed()
                if key[pygame.K_e]:
                    questionpage = True
                    play = False
                    #currentroom.locked = False
            else : question_notif = False

        else:
            # 3 detik black screen pas mau ganti room
            if (startpause+3)<time.time():
                change = False
                locked = currentroom.locked
                if currentroom.left==None and currentroom.right==None:
                    double_door = pygame.image.load("room.png").convert_alpha()
                elif currentroom.left==None:
                    double_door = pygame.image.load("door left.png").convert_alpha()
                elif currentroom.right==None:
                    double_door = pygame.image.load("door right.png").convert_alpha()
                else:
                    double_door = pygame.image.load("double door.png").convert_alpha()
                print('tree: level',currentroom.level,', index',currentroom.index)
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
            if currentroom.right != None:
                currentroom = currentroom.right

        # enable return
        if currentroom != mainroom and potato_y > 560:
            startpause= time.time()
            locked = False
            potato_x = 350
            potato_y = 200
            change = True
            currentroom = currentroom.previous
        
        if currentroom.powerUp==True:       #ngambil power up
            if potato_x>330 and potato_x<470 and potato_y<300 and potato_y>160:
                getpower = pygame.key.get_pressed()
                if getpower[pygame.K_e]:
                    getpowerup()
                    
    elif questionpage:
        exit = pygame.key.get_pressed()
        draw_question()
        if exit[pygame.K_ESCAPE]:
            questionpage = False
            play = True

        elif exit[pygame.K_n] or currentroom.Question.isAnswered:
            questionpage = False
            play = True
            currentroom.locked = False

    pygame.display.update()

pygame.quit()
