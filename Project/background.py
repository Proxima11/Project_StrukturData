import pygame
from StrukturData import Cave
from questions import question
import time
import queue as q
import os


pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
FPS = 60
score = 0

# if os.path.exists('score.txt'):
#     with open('score.txt', 'r') as file:
#         high_score = int(file.read())
# else:
#     high_score =0

fonts = pygame.font.SysFont('Chewy', 50)
fontHI = pygame.font.SysFont('calibri', 50, True,)




SCREEN_WIDTH = 840
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Potats Miner")

# basic font for user typed
base_font = pygame.font.Font(None, 60)
user_text = ''
  
# create rectangle
input_rect = pygame.Rect(300, 250, 400, 90)
  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color(95, 64, 18)
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color(167,111,28)
color = color_passive

active = False

#Struktur data
cave = Cave()
for i in range(52):
    cave.addRoomCave(i+1)
currentroom = cave.root
mainroom = cave.root

#tambah pertanyaan ke tiap ruangan
cave.addQuestion()
cave.printRoom()
cave.addTreasure()
cave.addTreasure()
cave.addTreasure()
cave.addTreasure()
cave.addTreasure()

#tambah powerup
cave.addPowerUp()
# queue untuk power up nantinya
queue = q.Queue()
queue.put(0)
queue.put(0)

# menu variable 
menu = True
hover_play = False
hover_highscore = False
hover_exit = False
hover_back = False
tutorialask = False
delaypress = 0

# tutorial variable
tutorial = False
yes_hover = False
no_hover = False
currenttutorial = 0
delay = 0.1
last = 0

# game variables
treasurefound = False
highscore = False
play = False
paused = False
gameover = False
locked = currentroom.locked
right = True
question_notif = False
loading = False
door1 = False
door2 = False
door3 = False
change = False
start_ticks=0
startpause = 0
powerupdelay = 0
escapedelay = 0
seconds = 300000
isdelay = False
leftdoor = False
rightdoor = False
questionpage = False
questionstart = 0
drawtime = 0
powerupoutput = ""
addtime = False
askname = False
username = ""
datascoreBOL = True

# pause
resume_hover = False
mainmenu_hover = False
pause_hover = False

# movement
potato_x = 350
potato_y = 450
mouse_x = 0
mouse_y = 0

# menu images
menu_bg = pygame.image.load("menubg.png").convert_alpha()
menu_blank = pygame.image.load("menublank.png").convert_alpha()
menu_play = pygame.image.load("menuplay.png").convert_alpha()
menu_highscore = pygame.image.load("menuhighscore.png").convert_alpha()
menu_exit = pygame.image.load("menuexit.png").convert_alpha()
game_title = pygame.image.load("gametitle.png").convert_alpha()
menu_potato = pygame.image.load("menupotato.png").convert_alpha()
highscore_page = pygame.image.load("highscorepage.png").convert_alpha()
highscore_back =  pygame.image.load("backbutton.png").convert_alpha()
highscore_backhover = pygame.image.load("backbuttonpressed.png").convert_alpha()
highscore_title = pygame.image.load("highscoretitle.png").convert_alpha()
game_pause = pygame.image.load("cave bg.jpg").convert_alpha()

#tutorial images
tutorial_confirm = pygame.image.load("tutorialconfirm.png").convert_alpha()
tutorial_yes = pygame.image.load("yesbutton.png").convert_alpha()
tutorial_no = pygame.image.load("nobutton.png").convert_alpha()
tutorial_yes_pressed = pygame.image.load("yespressed.png").convert_alpha()
tutorial_no_pressed = pygame.image.load("nopressed.png").convert_alpha()

tutorials = []
for i in range (0,13):
    tutorial = pygame.image.load(f"tutorial{i}.png").convert_alpha()
    tutorials.append(tutorial)

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

# paused images
paused_bg = pygame.image.load("gamepaused.png").convert_alpha()
resumebutton = pygame.image.load("resumebutton.png").convert_alpha()
resumehover = pygame.image.load("resumebuttonpressed.png").convert_alpha()
mainmenubutton = pygame.image.load("mainmenubutton.png").convert_alpha()
mainmenuhover = pygame.image.load("mainmenubuttonpressed.png").convert_alpha()
pausebutton = pygame.image.load("pausebutton.png").convert_alpha()
pausebuttonhover = pygame.image.load("pausebuttonpressed.png").convert_alpha()

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

#gameover images
asknamebg = pygame.image.load("nameinput.png").convert_alpha()
gameoverbg = pygame.image.load("gameover_score.png").convert_alpha()
gameoverpage = pygame.image.load("gameoverpage.png").convert_alpha()
treasurefoundpage = pygame.image.load("treasurefoundpage.png").convert_alpha()

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img, (x,y))

def draw_panel():
    draw_text('SCORE: ' + str(score),fonts,(225,255,255),120,30)

# def draw_high():
#     draw_text(str(high_score),fontHI,(255,255,255),355,270)

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

def draw_tutorial_confirm():
    screen.blit(tutorial_confirm, (0,0))
    screen.blit(tutorial_yes, (0,0))
    screen.blit(tutorial_no, (0,0))

    if yes_hover:
        screen.blit(tutorial_yes_pressed, (0,0))
    elif no_hover:
        screen.blit(tutorial_no_pressed, (0,0))

def draw_tutorial():
    screen.blit(tutorials[currenttutorial], (0,0))

def highscores():
    screen.blit(highscore_page, (0,0))
    counter = 0
    top5_score = []
    with open('score.txt') as file_score:
        while True:
            counter+=1
            line = file_score.readline()
            if not line:
                break
            elif counter <= 5:
                collect_score = [scores.split(';') for scores in line]
                top5_score.append(collect_score)
            else:
                break
    font = pygame.font.SysFont('freesansbold.ttf',22)
    for i in range(len(top5_score)):
        white = (255,255,255)
        str_i = str(i+1)
        str_nama = str(top5_score[i][0])
        str_score = str(top5_score[i][1])
        counter_surface = font.render(str_i, True, white)
        nama_surface = font.render(str_nama, True, white)
        score_surface = font.render(str_score, True, white)
        if i == 0:
            screen.blit(counter_surface, (202,195))
            screen.blit(nama_surface, (202,225))
            screen.blit(score_surface, (202,255))
        elif i == 1:
            screen.blit(counter_surface, (423,192))
            screen.blit(nama_surface, (423,212))
            screen.blit(score_surface, (202,242))
        elif i == 2:
            screen.blit(counter_surface, (313,249))
            screen.blit(nama_surface, (313,279))
            screen.blit(score_surface, (313,309))
        elif i == 3:
            screen.blit(counter_surface, (204,308))
            screen.blit(nama_surface, (204,338))
            screen.blit(score_surface, (204,368))
        elif i == 4:
            screen.blit(counter_surface, (429,293))
            screen.blit(nama_surface, (429,323))
            screen.blit(score_surface, (429,353))

    
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

def draw_highscore():
    screen.blit(highscore_page, (0,0))
    screen.blit(highscore_title, (0,0))
    screen.blit(highscore_back, (0,0))
    if hover_back: screen.blit(highscore_backhover, (0,0))

    counter = 0
    top5_score = []
    with open('score.txt') as file_score:
        while True:
            line = file_score.readline()
            if not line:
                break
            elif line == "\n":
                continue
            elif line == "":
                continue
            else :
                counter+=1
                if counter <= 5:
                    collect_score = line.split(';')
                    top5_score.append(collect_score)
                else:
                    break
    font = pygame.font.SysFont('freesansbold.ttf',26)
    for i in range(len(top5_score)):
        white = (255,255,255)
        str_i = str(i+1)
        str_nama = str(top5_score[i][0])
        str_score = ""
        temp = str(top5_score[i][1])
        angka = ["0","1","2","3","4","5","6","7","8","9"]
        for j in temp:
            if j in angka:
                str_score += j
        counter_surface = font.render(str_i, True, white)
        nama_surface = font.render(str_nama, True, white)
        score_surface = font.render(str_score, True, white)
        if i == 0:
            screen.blit(counter_surface, (270,260))
            screen.blit(nama_surface, (265,280))
            screen.blit(score_surface, (265,300))
        elif i == 1:
            screen.blit(counter_surface, (575,255))
            screen.blit(nama_surface, (565,275))
            screen.blit(score_surface, (565,295))
        elif i == 2:
            screen.blit(counter_surface, (425,335))
            screen.blit(nama_surface, (415,355))
            screen.blit(score_surface, (415,375))
        elif i == 3:
            counter_surface = pygame.transform.rotate(counter_surface, 30)
            nama_surface = pygame.transform.rotate(nama_surface, 30)
            score_surface = pygame.transform.rotate(score_surface, 30)
            screen.blit(counter_surface, (270,415))
            screen.blit(nama_surface, (275,428))
            screen.blit(score_surface, (290,455))
        elif i == 4:
            screen.blit(counter_surface, (590,400))
            screen.blit(nama_surface, (580,420))
            screen.blit(score_surface, (580,440))
    #draw_high()
    #screen.blit(highscore_back,(0,400))
    

def game_over():
    screen.blit(highscore_page, (0,0))
    screen.blit(highscore_title, (0,0))


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
    powerup1 = queue.queue[0]
    powerup2 = queue.queue[1]

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

def usePowerUp() -> str:
    use = queue.queue[0]
    notification = ""
    used = True
    
    if use == 0:
        notification = "tidak ada power up"
    elif use == 1:
        notification = "waktu ditambahkan"
        pass
    elif use == 2:
        found = cave.poweruproot(currentroom)
        print(found)
        if found:
            notification = "treasure berada di anak gua ini"
        else :
            notification = "treasure tidak berada di anak gua ini"
    elif use == 3:
        level = cave.poweruplevel()
        print(level)
        notification = "treasure berada pada level - " + str(level)
    elif use == 4:
        if currentroom.Question.count == 2:
            notification = "treasure tidak dapat digunakan"
            used = False
        else : notification = "tembok dibuka"
    if use != 0 and used:
        queue.put(0)
        queue.get()

    return notification
    
# buat ngambil powerupnya pencet E
def getpowerup():
    queue1 = queue.get()
    queue2 = queue.get()

    if queue1 != 0: queue.put(queue1)
    if queue2 != 0: queue.put(queue2)
    queue.put(currentroom.powerUptype)

    if queue.qsize() > 2: queue.get()
    elif queue.qsize() == 1 : queue.put(0)

    currentroom.powerUp=False
    currentroom.powerUptype=0

def draw_question_():
    
    if currentroom.Question is not None and not currentroom.Question.isAnswered:
        white = (255, 255, 255)
        font = pygame.font.SysFont('freesansbold.ttf',28)
        collection = [word.split('/') for word in currentroom.Question.question.splitlines()]
        space = font.size(' ')[0]
        pos = (110,75)
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
        temp_y = temp_y + 24

def draw_question(start_ticks):
    global score
    screen.blit(questionbg,(0,0))
    screen.blit(choice1,(0,0))
    screen.blit(choice2,(0,0))
    if len(currentroom.Question.answer) > 2:
        screen.blit(choice3,(0,0))
        screen.blit(choice4,(0,0))
    draw_seconds()
    draw_question_()
    draw_answer1()
    draw_answer2()
    draw_answer3()
    draw_answer4()
    start_ticks -= cclock
    if seconds<=0:
        return -9999
    if cave.isAllAnswered():
        return -9999
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x > 115 and mouse_x < 350 and mouse_y > 255 and mouse_y < 390:
        click = pygame.mouse.get_pressed()
        if click[0]:
            currentroom.Question.isAnswered = True
            if not currentroom.Question.isCorrect(currentroom.Question.answer[0]):
                start_ticks -= 5000
            else:
                score+=100
            currentroom.locked = False
    #235
    if mouse_x > 415 and mouse_x < 750 and mouse_y > 255 and mouse_y < 390:
        click = pygame.mouse.get_pressed()
        if click[0]:
            currentroom.Question.isAnswered = True
            if not currentroom.Question.isCorrect(currentroom.Question.answer[1]):
                start_ticks -= 5000
            else:
                score+=100
            currentroom.locked = False
    #135
    if mouse_x > 115 and mouse_x < 350 and mouse_y > 415 and mouse_y < 550 and len(currentroom.Question.answer) > 2:
        click = pygame.mouse.get_pressed()
        if click[0]:
            currentroom.Question.isAnswered = True
            if not currentroom.Question.isCorrect(currentroom.Question.answer[2]):
                start_ticks -= 5000
            else:
                score+=100
            currentroom.locked = False
    
    if mouse_x > 415 and mouse_x < 750 and mouse_y > 415 and mouse_y < 550 and len(currentroom.Question.answer) > 2:
        click = pygame.mouse.get_pressed()
        if click[0]:
            currentroom.Question.isAnswered = True
            if not currentroom.Question.isCorrect(currentroom.Question.answer[3]):
                start_ticks -= 5000
            else:
                score+=100
            currentroom.locked = False        
    return start_ticks

def draw_seconds():
    font_seconds = pygame.font.SysFont('freesansbold.ttf',32)
    second_surface = font_seconds.render('Time: '+str(int(seconds / 1000)), True, (255,255,255), (255,0,0))
    screen.blit(second_surface,(730,10))

def draw_askname():
    screen.blit(asknamebg, (0,0))

def draw_gameover():
    if treasurefound : screen.blit(treasurefound, (0,0))
    else : screen.blit(gameoverpage, (0,0))

def draw_paused():
    screen.blit(paused_bg, (0,0))
    screen.blit(resumebutton, (0,0))
    screen.blit(mainmenubutton, (0,0))
    
    if mainmenu_hover: screen.blit(mainmenuhover, (0,0))
    if resume_hover: screen.blit(resumehover, (0,0))

def draw_pausebutton():
    screen.blit(pausebutton, (0,0))

    if pause_hover: screen.blit(pausebuttonhover, (0,0))

run = True

#game play
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    cclock = clock.tick(FPS)
    
    if menu:
        draw_menu()
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_x>520 and mouse_x<680 and mouse_y > 200 and mouse_y < 280 and not tutorialask:
            hover_play = True
            click = pygame.mouse.get_pressed()
            if click[0]:
                tutorialask = True 
        else : hover_play = False

        if mouse_x>500 and mouse_x<650 and mouse_y > 290 and mouse_y < 350 and not tutorialask and delaypress+1.5<time.time():
            hover_highscore = True
            click = pygame.mouse.get_pressed()
            if click[0]:
                highscore = True
                menu = False
        else : hover_highscore = False

        if mouse_x>500 and mouse_x<650 and mouse_y > 380 and mouse_y < 450 and not tutorialask:
            hover_exit = True
            click = pygame.mouse.get_pressed()
            if click[0]: run = False
        else : hover_exit = False

        if tutorialask:
            draw_tutorial_confirm()
            if mouse_x>170 and mouse_x<370 and mouse_y > 250 and mouse_y < 380:
                yes_hover = True
                click = pygame.mouse.get_pressed()
                if click[0] : 
                    menu = False
                    tutorialask = False
                    tutorial = True
            else: yes_hover = False

            if mouse_x>430 and mouse_x<630 and mouse_y > 250 and mouse_y < 380:
                no_hover = True
                click = pygame.mouse.get_pressed()
                if click[0] : 
                    menu = False
                    tutorialask = False
                    tutorial = False
                    start_ticks=time.time()
                    play = True
            else: no_hover = False
    elif highscore:
        draw_highscore()
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_x > 740 and mouse_x < 820 and mouse_y < 80 and mouse_y > 10:
            hover_back = True
            click = pygame.mouse.get_pressed()
            if click[0]:
                menu = True
                highscore = False
        else : hover_back = False

    elif tutorial:
        
        now = time.time()
        draw_tutorial()
        nextprev = pygame.key.get_pressed()

        if nextprev[pygame.K_LEFT] and ((now-last) > delay):
            currenttutorial -= 1
            last = now
            if currenttutorial < 0: currenttutorial = 0
        if nextprev[pygame.K_RIGHT] and ((now-last) > delay):
            currenttutorial += 1
            last = now
            if currenttutorial > 12: currenttutorial = 12
        
        if nextprev[pygame.K_RETURN] and currenttutorial == 12:
            tutorial = False
            currenttutorial = 0
            start_ticks=time.time()
            play = True

    elif play:
        if not change:

            skip = pygame.key.get_pressed()
            if skip[pygame.K_s]: seconds = 10
            # menentukan bentuk ruangan
            if currentroom.left != None:
                leftdoor = True
            else: leftdoor = False
            if currentroom.right != None:
                rightdoor = True
            else: rightdoor = False

            # status locked
            locked = currentroom.locked

            # power up
            usePU = pygame.key.get_pressed()
            if usePU[pygame.K_p] and powerupdelay+3<time.time(): 
            #di kasih delay biar gak kepake e cuma 1 dalam 3 detik
                powerupdelay = time.time()
                drawtime = 3000
                powerupoutput = usePowerUp()
                print(powerupoutput)
                addtime = True

            # power up time
            if powerupoutput == "waktu ditambahkan" and addtime:
                seconds += 10000
                addtime = False

            if powerupoutput == "tembok dibuka":
                currentroom.locked = False

            #gambar ruangan
            draw_room()

            # gambar powerup
            if not locked:
                draw_powerup()
            
            # gambar treasure
            draw_treasure()
            
            # gambar potato
            draw_potato()

            # gambar help powerup
            draw_held_powerup()

            draw_panel()

            if currentroom.treasure:
                if potato_x>300 and potato_x<420 and potato_y<300:
                    gettreasure = pygame.key.get_pressed()
                    font_notif = pygame.font.SysFont('freesansbold.ttf',32)
                    notif_surface = font_notif.render('Press space to take the treasure', True, (255,255,255), (0,0,0))
                    screen.blit(notif_surface, (SCREEN_WIDTH // 2-150 , 220))
                    if gettreasure[pygame.K_SPACE]:
                        currentroom.treasure = False
                        score += 1000



            #timer
            if not paused: seconds-=cclock
            else : seconds = seconds

            draw_seconds()

            if seconds<=0:
                play=False
                askname = True

            # draw notification powerup
            if drawtime > 0 and not paused:
                drawtime -= cclock
                if drawtime < 0: drawtime = 0
                text = my_font.render(powerupoutput, False, (255,255,255))
                text_x, text_y = text.get_size()
                screen.blit(text, ((SCREEN_WIDTH - text_x) / 2 , 200))

            pausegame = pygame.key.get_pressed()
            if pausegame[pygame.K_ESCAPE] and escapedelay+1.5<time.time(): 
                paused = True
            
            if paused:
                draw_paused()
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                keyboard = pygame.key.get_pressed()
                if keyboard[pygame.K_c]: paused = False
                if keyboard[pygame.K_m]:
                    delaypress = time.time() 
                    # redraw cave
                    cave = Cave()
                    for i in range(52):
                        cave.addRoomCave(i+1)
                    currentroom = cave.root
                    mainroom = cave.root

                    #tambah pertanyaan ke tiap ruangan
                    cave.addQuestion()
                    cave.printRoom()

                    #bikin 5 treasure
                    cave.addTreasure()
                    cave.addTreasure()
                    cave.addTreasure()
                    cave.addTreasure()
                    cave.addTreasure()

                    #tambah powerup
                    cave.addPowerUp()

                    # refresh queue
                    queue = q.Queue()
                    queue.put(0)
                    queue.put(0)

                    # variable
                    menu = True
                    tutorialask = False
                    tutorial = False
                    currenttutorial = 0
                    delay = 0.1
                    last = 0

                    # game variables
                    highscore = False
                    play = False
                    paused = False
                    gameover = False
                    right = True
                    question_notif = False
                    loading = False
                    change = False
                    start_ticks=0
                    startpause = 0
                    powerupdelay = 0
                    seconds = 300000
                    isdelay = False
                    questionstart = 0
                    drawtime = 0
                    score = 0
                    potato_x = 350
                    potato_y = 450
                    mouse_x = 0
                    mouse_y = 0

                if mouse_x>100 and mouse_x<370 and mouse_y > 250 and mouse_y < 380:
                    resume_hover = True
                    click = pygame.mouse.get_pressed()
                    if click[0] : paused = False
                else: resume_hover = False

                if mouse_x>480 and mouse_x<800 and mouse_y > 250 and mouse_y < 380:
                    mainmenu_hover = True
                    click = pygame.mouse.get_pressed()
                    if click[0] : 
                        cave = Cave()
                        for i in range(52):
                            cave.addRoomCave(i+1)
                        currentroom = cave.root
                        mainroom = cave.root

                        #tambah pertanyaan ke tiap ruangan
                        cave.addQuestion()
                        cave.printRoom()

                        #bikin 5 treasure
                        cave.addTreasure()
                        cave.addTreasure()
                        cave.addTreasure()
                        cave.addTreasure()
                        cave.addTreasure()

                        #tambah powerup
                        cave.addPowerUp()

                        # refresh queue
                        queue = q.Queue()
                        queue.put(0)
                        queue.put(0)

                        # variable
                        menu = True
                        tutorialask = False
                        tutorial = False
                        currenttutorial = 0
                        delay = 0.1
                        last = 0

                        # game variables
                        highscore = False
                        play = False
                        paused = False
                        gameover = False
                        right = True
                        question_notif = False
                        loading = False
                        change = False
                        start_ticks=0
                        startpause = 0
                        powerupdelay = 0
                        seconds = 300000
                        isdelay = False
                        questionstart = 0
                        drawtime = 0
                        score = 0
                        potato_x = 350
                        potato_y = 450
                        mouse_x = 0
                        mouse_y = 0
                else: mainmenu_hover = False
            else :
                draw_pausebutton()
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_x > 10 and mouse_x < 100 and mouse_y > 10 and mouse_y < 80: 
                    pause_hover = True
                    click = pygame.mouse.get_pressed()
                    if click[0] : paused = True
                else : pause_hover = False

            move = pygame.key.get_pressed()
            if potato_y >= 450 and currentroom != mainroom and not paused:
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
            elif potato_y > 300 and not paused:
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
            elif potato_y > 160 and not paused:
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
                if not paused:
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
            if ((potato_x > 250 and potato_x < 500) and (potato_y < 400 and potato_y > 350)) and locked is not False and not paused: 
                question_notif = True
                key = pygame.key.get_pressed()
                if key[pygame.K_e]:
                    questionstart = time.time()
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
        
        #ngambil power up
        if currentroom.powerUp==True: 
            if potato_x>330 and potato_x<470 and potato_y<300 and potato_y>160:
                getpower = pygame.key.get_pressed()
                font_notif = pygame.font.SysFont('freesansbold.ttf',32)
                notif_surface = font_notif.render('Press E to take the power up', True, (255,255,255), (0,0,0))
                screen.blit(notif_surface, (SCREEN_WIDTH // 2-120 , 220))
                if getpower[pygame.K_e]:
                    getpowerup()
        
                    
    elif questionpage:
        exit = pygame.key.get_pressed()
        seconds =  draw_question(seconds)
        if seconds <= 0:
            play=False
            askname = True
            questionpage = False
        seconds-= cclock
        draw_seconds()
        if seconds<=0:
            play=False
            askname = True
        if cave.isAllAnswered():
            play=False
            askname = True

        questiontime = int(time.time()-questionstart)
        if exit[pygame.K_ESCAPE] and escapedelay+1.5<time.time():
            escapedelay = time.time()
            questionpage = False
            play = True
        elif exit[pygame.K_n] or currentroom.Question.isAnswered:
            questionpage = False
            play = True
            currentroom.locked = False
    
    elif askname:
        draw_askname()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_RETURN:
                    askname = False
                    gameover = True
                    delaypress = time.time()
                    username = user_text
                    print(username)
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif len(user_text) <= 11:
                    user_text += event.unicode
            
            if active:
                color = color_active
            else:
                color = color_passive
            
        pygame.draw.rect(screen, color, input_rect)
    
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        input_rect.w = max(100, text_surface.get_width()+10)
        
        pygame.display.flip()
    elif gameover:
        if datascoreBOL:
            f = open("score.txt", "a")
            strings = username + ";" + str(score)
            f.write(strings+"\n")
            f.close()
            all_scores = []
            with open('score.txt') as file_scoreX:
                while True:
                    lines = file_scoreX.readline()
                    if not lines:
                        break
                    elif lines == "\n":
                        continue
                    elif lines == "":
                        continue
                    else:
                        collect_scoreS = lines.split(';')
                        all_scores.append(collect_scoreS)
    
            #
            swapped = False
            n = len(all_scores)
            angka = ["1","2","3","4","5","6","7","8","9","0"]
            for i in range(n-1):
                for j in range(0, n-i-1):
                    temp1 = all_scores[j][1]
                    temp2 = all_scores[j+1][1]
                    str1 = ""
                    str2 = ""
                    for chrs in temp1:
                        if chrs in angka:
                            str1+=chrs
                    for chrs in temp2:
                        if chrs in angka:
                            str2+=chrs
                    if int(str1) < int(str2):
                        swapped = True
                        all_scores[j], all_scores[j + 1] = all_scores[j + 1], all_scores[j]
                if not swapped:
                    break
                    
                
            fo = open("score.txt", "w")
            fo.truncate()
            for k in range(len(all_scores)):
                stringss = str(all_scores[k][0]+";"+str(all_scores[k][1])+"\n")
                fo.write(stringss)
            fo.close()
            
            datascoreBOL = False

        print(username)
        draw_gameover()
        backtomenu = pygame.key.get_pressed()
        writescore = my_font.render(str(score), True, (255,255,255))
        screen.blit(writescore, (600, 255))
        # if score > high_score:
        #     high_score = score
        #     with open('score.txt', 'w') as file:
        #         file.write(str(high_score))
        if backtomenu[pygame.K_RETURN] and delaypress+1.5<time.time():
            
            # redraw cave
            cave = Cave()
            for i in range(52):
                cave.addRoomCave(i+1)
            currentroom = cave.root
            mainroom = cave.root

            #tambah pertanyaan ke tiap ruangan
            cave.addQuestion()
            cave.printRoom()

            #bikin 5 treasure
            cave.addTreasure()
            cave.addTreasure()
            cave.addTreasure()
            cave.addTreasure()
            cave.addTreasure()

            

            #tambah powerup
            cave.addPowerUp()

            # refresh queue
            queue = q.Queue()
            queue.put(0)
            queue.put(0)

            # variable
            menu = True
            tutorialask = False
            tutorial = False
            currenttutorial = 0
            delay = 0.1
            last = 0

            # game variables
            highscore = False
            play = False
            paused = False
            gameover = False
            right = True
            question_notif = False
            loading = False
            change = False
            start_ticks=0
            startpause = 0
            powerupdelay = 0
            seconds = 300000
            isdelay = False
            questionstart = 0
            drawtime = 0
            score = 0
            potato_x = 350
            potato_y = 450
            mouse_x = 0
            mouse_y = 0


    pygame.display.update()
pygame.quit()
