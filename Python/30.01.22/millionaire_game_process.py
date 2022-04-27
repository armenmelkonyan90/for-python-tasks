#!/bin/python3
import random
import sys
#correct_answers = 0
#incorrect_answers = 0
def get_questions():
    with open("millionaire_quetions.txt") as f:
            question = f.readlines()
    return question
def get_answers():
    with open("millionaire_answers.txt") as f:
            true_answers = f.readlines()
    return true_answers
#def fifty_fifty(gq, ga, qnum):
#    ql=gq[qnum]
#    new_answers = ""
#    for i in range(len(ql)):
#        if ql[i] != ga[qnum]:
#            new_answers +=gl[i]
#            break
#    new_answers += 

       
    

def game_process():
    qnum_list = []
    count = 0
    correct_answers = 0
    gq =get_questions()
    while True:
        qnum = random.randint(0, len(gq)-1)
        if qnum in qnum_list:
            continue
        qnum_list.append(qnum)
        count +=1
        print(gq[qnum].replace("\\","\n"))
        answer = input("enter your answer: ")
        ga = get_answers()
        for true_answer in ga:
            if answer+"\n" == true_answer:
                print("correct answer\n\n")
                correct_answers += 1
                break
#            if answer == "50/50":
#                fifty_fifty(gq, ga, qnum)
        else:
            print("wrong: The correct answer is", ga[qnum], "\n\n")
            if count == 10:
                break
    print("GAME OWER!!!\nYou have a", correct_answers, "correct answers out of 10")
    return int(correct_answers)
def get_results(fname):
    with open(fname) as f:
        return f.readlines()
def create_result(data_list):
    gamer_list = {}
    for el in data_list:
        el = el.replace("\n", "")
        el = el.replace(" ", "")
        tmp = el.split("-")
        gamer_list[tmp[0]] = int(tmp[1])
#    gamer_list = dict(sorted(gamer_list.items(), reverse = True, key = lambda x: x[1]))
    return gamer_list
def sort_result(gamer_list):
    sorted_list = dict(sorted(gamer_list.items(), reverse = True, key = lambda x: x[1]))
   # print(sorted_list)
    return sorted_list
def write_in_file(fname, sorted_list):
    with open(fname, "w") as f:
        for k,v in sorted_list.items():
            f.write(k + " - " + str(v) + "\n")
def main():
    fname = "gamer_list.txt"
    result = get_results(fname)
    gl = create_result(result)
   # sl = sort_result(gl)
    print("Welcome to the game. MILLIONAIRE.\nWe start ")
    gamer = input("enter your name: ")
    if gamer in gl:
         print("Hello ",gamer, "have a good game")
         
         gl[gamer] = game_process()

    else:
        ans = input("you are not registered in the game. do you want registre? y/n")
        if ans.lower() == "n":
            print("BYE")
        else:

            print("Hello ",gamer, "have a good game")
            gl[gamer] =game_process()
    sl = sort_result(gl)
    write_in_file(fname, sl)
if __name__ == "__main__":
    main()

