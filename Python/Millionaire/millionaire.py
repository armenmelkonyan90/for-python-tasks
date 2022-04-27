#!/usr/bin/python3
import time
from tkinter import *
from tkinter import messagebox
import random
import pygame
pygame.init()

W = 1000
H = 800

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,102,204)
GREEN = (0,255,0)
display = pygame.display.set_mode((W,H), pygame.DOUBLEBUF)
pygame.display.set_caption("MILLIONAIRE")
logo = pygame.image.load("images/logo.png")
pygame.display.set_icon(logo)
pygame.display.update()
font=pygame.font.SysFont('arial', 18, bold=True)
font1=pygame.font.SysFont('arial', 25, bold=True)
gamer_name=""

def open_():
    global gamer_name
    pygame.mixer.music.load("sounds/01.mp3")
    pygame.mixer.music.play()
    background = pygame.image.load("images/hall.jpg")
    button_play = pygame.image.load("images/button_play.png")
    button_quit = pygame.image.load("images/button_quit.png")
    display.blit(background, (0,0))
    display.blit(button_play, (20,20))
    display.blit(button_quit, (20,80))
    pygame.display.update()
    while True:
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif pressed[0] and 20 < pos[0] < 120 and 80 < pos[1] <130:
                print("o")
                pygame.quit()
                exit()
            else:

                if pressed[0]==1 and 20 < pos[0] < 120 and 20 < pos[1] < 70:
                    name = press_play()
                    gamer_name=name
                    return name
        
gamer_name=""
def press_play():

    pygame.mixer.music.load("sounds/02.mp3")
    pygame.mixer.music.play()
    root = Tk()
    root.geometry("300x300+650+300")
    root.title("signin")
    text_log = Label(text="login")
    login = Entry()
    text_pass = Label(text="password")
    password = Entry(show="*")
    button_signup = Button(text="Signup", command=lambda: log_db())
    button_signin = Button(text="Signin", command = lambda: signin())
    text_log.pack()
    login.pack()
    text_pass.pack()
    password.pack()
    button_signin.pack()
    button_signup.pack()
    def log_db():
        with open(".data.txt", "a") as f:
            f.write(str(login.get())+"-"+str(password.get())+"\n")
    def signin():
        global gamer_name
        with open(".data.txt") as f:
            cont = f.readlines()

        gamer_list={}
        for el in  cont:
            el=el.replace("\n", "")
            tmp=el.split("-")
            gamer_list[tmp[0]] = tmp[1]
        if login.get() in gamer_list:
            if password.get() == gamer_list[login.get()]:
                gamer_name = login.get()
                 
                root.destroy()

            else:
                messagebox.showerror("Error","incorrect password")
        else:
            messagebox.showerror("Error","incorrect login")
    
    root.mainloop()
    
    return gamer_name

def welcome(name):
    pygame.mixer.music.load("sounds/02.mp3")
    pygame.mixer.music.play(0, 0.0, 15)
    display.fill(BLACK)
    background = pygame.image.load("images/hall1.jpg")
    display.blit(background, (0,0))
    pygame.display.update()
    surf = pygame.Surface((1000, 200))
    surf.fill(BLUE)
    display.blit(surf,(0, 667))
    pygame.display.update()
    message = "Ladies and Gentlemen! Welcome to a new round of WHO WANTS TO BE A MILLIONAIRE?!"
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 675))
    time.sleep(2)
    pygame.display.update()
    time.sleep(3)
    message = "Hello, welcome to Who Wants to be a Millionaire!?. Let's start the game"
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 700))
    pygame.display.update()
    time.sleep(3)
    message = f'Hello! Im {name}'
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 725))
    pygame.display.update()
    time.sleep(3)
    message = 'I am very glad to see you!!! I am ready'
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 750))
    pygame.display.update()

    pygame.mixer.music.load("sounds/applause.mp3")
    pygame.mixer.music.play()
    time.sleep(1)
    message ="Press Enter to continue"
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 775))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rules()
def rules():
    pygame.mixer.music.load("sounds/03.mp3")
    pygame.mixer.music.play(0, 0.0, 15)
    display.fill(BLACK)
    background = pygame.image.load("images/hall2.jpg")
    display.blit(background, (0,0))
    pygame.display.update()
    surf = pygame.Surface((1000, 200))
    surf.fill(BLUE)
    display.blit(surf,(0, 667))
    pygame.display.update()
    message = "According to the new rules of our game, you must answer 10 questions"
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 675))
    time.sleep(2)
    pygame.display.update()
    time.sleep(2)
    message = "each correct answer will bring you 1000 points "
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 700))
    pygame.display.update()
    time.sleep(2)
    message ="at the end of the game you will receive a cash amount equal to your points "
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 725))
    pygame.display.update()
    time.sleep(2)
    pygame.mixer.music.load("sounds/applause.mp3")
    pygame.mixer.music.play()
    message ="Press Enter to START"
    text=font.render(message, 1, BLACK)
    display.blit(text, (25, 750))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_game_process()
                    
def get_questions():
    with open("millionaire_quetions.txt") as f:
            questions = f.readlines()

    return questions
def get_answers():
    with open("millionaire_answers.txt") as f:
        true_answers=[]
        true_answers1 = f.readlines()
        for el in true_answers1:
            true_answers.append(el.split())
    return true_answers
def question_numbers():

    qnum_list=[]
    while len(qnum_list)<10:
        qnum = random.randint(0, 19)
        if qnum  in qnum_list:
            continue
        else:
            qnum_list.append(qnum)   
    print(qnum_list)
    for i in qnum_list:
        yield i
def game_bg():
    pygame.mixer.music.load("sounds/04.mp3")
    pygame.mixer.music.play(-1)
    display.fill(BLACK)
    background = pygame.image.load("images/hall3.jpg").convert_alpha()
    display.blit(background, (0,0))
    question_bord =pygame.image.load("images/qb.png").convert_alpha()
    question_bord.set_colorkey((0,0,0))
    display.blit(question_bord, (102,500))
    pygame.display.update()

def start_game_process():
    game_bg()
    ten_questions()
count=0
points=0

def pol(display, pos):
    bc = [[187,455,615,663],[187,455,683,731],[552,820,615,663],[552,820,683,731]]
    yellow_pol = pygame.image.load("images/yellow_pol1.png").convert_alpha()
    if bc[0][0]<pos[0]<bc[0][1] and bc[0][2]<pos[1]<bc[0][3]:
        display.blit(yellow_pol,(155,611))
    elif bc[1][0]<pos[0]<bc[1][1] and bc[1][2]<pos[1]<bc[1][3]:
         display.blit(yellow_pol, (155,676))
    elif bc[2][0]<pos[0]<bc[2][1] and bc[2][2]<pos[1]<bc[2][3]:
         display.blit(yellow_pol, (507,611))
    else:
        display.blit(yellow_pol, (507,676))
    pygame.display.update()
def true_pol(display, ta):
    bc = [[187,455,615,663],[187,455,683,731],[552,820,615,663],[552,820,683,731]]
    true_pol = pygame.image.load("images/true_pol.png").convert_alpha()
    if int(ta[0])==bc[0][0]:
        if int(ta[1])==bc[0][2]:
            display.blit(true_pol, (155,611))
        else:
            display.blit(true_pol, (155,676))
    elif int(ta[0])==bc[2][0]:
        if int(ta[1])==bc[2][2]:
            display.blit(true_pol, (507,611))
        else:
            display.blit(true_pol, (507,676))
i=question_numbers()


def ten_questions():
    global count, points, i
    pygame.mixer.music.load("sounds/04.mp3")
    pygame.mixer.music.play(-1)
    cord_list=[[190,550],[190,630],[550,630],[190,693],[550,693]]

    questions=get_questions()
    true_answers=get_answers()
#    i=question_numbers()
    qnum=next(i)
    question=questions[qnum].replace("\n","").split("\\")
    ta=true_answers[qnum]
    print(ta)
    text=font.render(question[0], 1, BLACK)
    display.blit(text, cord_list[0])
    text=font.render(question[1], 1, BLACK)
    display.blit(text, cord_list[1])
    text=font.render(question[2], 1, BLACK)
    display.blit(text, cord_list[2])
    text=font.render(question[3], 1, BLACK)
    display.blit(text, cord_list[3])
    text=font.render(question[4], 1, BLACK)
    display.blit(text, cord_list[4])
    pygame.display.update()
    while True:
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
   
            if pressed[0]==1:
                if 190<pos[0]<460 or 550 < pos[0] < 820:
                    if 630 < pos[1] < 670 or 690 < pos[1] < 730:
                        if int(ta[0])<pos[0]<int(ta[2]) and int(ta[1])<pos[1]<int(ta[3]):
                            pygame.mixer.music.load("sounds/Correct.mp3")
                            pygame.mixer.music.play()
                            true_pol(display,ta)
                            pygame.display.update()
                            points+=1000
                            time.sleep(2)
                            game_bg()
                            count+=1
                            if count !=10:
                                ten_questions()
                            else:
                                write_results()
                                end_game()

                        else:
                            pygame.mixer.music.load("sounds/Incorrect.mp3")
                            pygame.mixer.music.play()
                            pol(display, pos)
                            time.sleep(1)
                            true_pol(display, ta)
                            pygame.display.update()
                            time.sleep(2)
                            game_bg()
                            count+=1
                            if count !=10:
                                ten_questions()
                            else:
                                write_results()
                                end_game()
def write_results():
    with open("gamer_list.txt") as f:
        results=f.readlines()

    gamer_list = {}
    for el in results:
        el = el.replace("\n", "")
        el = el.replace(" ", "")
        tmp = el.split("-")
        if tmp[0] == gamer_name:
            gamer_list[tmp[0]] = str(points)
        else:
            gamer_list[tmp[0]] = tmp[1]
        
     
    sorted_list = dict(sorted(gamer_list.items(), reverse = True, key = lambda x: x[1]))

    with open("gamer_list.txt", "w") as f:
        for k,v in sorted_list.items():
            f.write(k + " - " + str(v) + "\n")
                    
                    
def end_game():
    pygame.mixer.music.load("sounds/01.mp3")
    pygame.mixer.music.play()
    background = pygame.image.load("images/hall.jpg")
    button_play = pygame.image.load("images/button_play.png")
    button_quit = pygame.image.load("images/button_quit.png")
    display.blit(background, (0,0))
    display.blit(button_play, (20,20))
    display.blit(button_quit, (20,80))
    pygame.display.update()
    pygame.draw.rect(display, BLUE, (150,300,700,50))
    message = f'CONGRATULATION {gamer_name}!!! YOU EARN {points} POINTS!!!' 
    text=font1.render(message, 1, BLACK)
    display.blit(text, (163, 315))
    pygame.display.update()

    while True:
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif pressed[0] and 20 < pos[0] < 120 and 80 < pos[1] <130:
                print("o")
                pygame.quit()
            else:

                if pressed[0]==1 and 20 < pos[0] < 120 and 20 < pos[1] < 70:
                    name = press_play()
                    return name


FPS = 60
clock = pygame.time.Clock()

def main():

    name=open_()
    welcome(name)
if __name__ == "__main__":
    main()

