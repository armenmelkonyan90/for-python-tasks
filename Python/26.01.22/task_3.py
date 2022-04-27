#!/bin/python3
new_pas = ""
confpas = ""
users = {'vaxo1997': '1357a', 'srtaker': 9876, 'poxospoxosyan': '1245'}
login = input("enter login: ")
for k in users:
    if k == login:
        pas = input("Enter password: ")
        if pas == users[k]:
            print("you are sign in")
            break
        else:
            pas1 = input("Wrong password, try again")
        if pas1 == users[k]:
            print("you are sign in")
            break
        else:
            pas2 = input("you entered the wrong password you have one more try")
        if pas2 == users[k]:
            print("you are sign in")
            break
        else:
            print("this user does not exist")
            break
    else:
        print("this user is not sign up in the system. ")
    answer = input("would you want to sign up? y/n  ")
    if answer.lower() == "y":
        new_pas = input("enter your password: ")
        confpas = input("confirm your password: ")
        if new_pas == confpas:
            users[login] = confpas
            print("you are signed up"):
            break
        else:
            print("Password mismatch")
            break
    else:
        break
print(users)
#    if pas == users[k]:
 #       print("you are sign in")
#    else:
#        pas1 = input("Wrong password, try again")
#    if pas1 == user[k]:
#        print("you are sign in")
#    else:
#        pas2 = input("you entered the wrong password you have one more try")
#    if pas2 == user[k]:
#        print("you are sign in")
#    else:
#        print("this user does not exist")
#        break
