#!/bin/python3
print("To exit the game, enter 'out'")
print()
print("Who was the first president of the USA: ")
answerboard = "----------"
correct_answer = "washington"
print(answerboard)
answerboard.split()
while True:
    if correct_answer == answerboard:
        print("Congratulation You WIN!!!")
        break
    letter = input("enter the letter: ")
    if letter == correct_answer:
         print("Congratulation You WIN!!!")
         break
    if letter == "out":
        print("GAME OVER")
        break
    if len(letter) == 0 or len(letter) > 1:
        print("don't break the rules")
    if letter in correct_answer:
        for i in range(len(correct_answer)):
            if correct_answer[i] == letter:
                answerboard = answerboard[:i] + letter + answerboard[i+1:]
                print("you are right, open the letter")
                print(answerboard.upper())
                
       
            
    else:
         print("Oh no... try again")
         print(answerboard.upper())
          
         
