#!/usr/bin/python3
longest_word = ""
while True:
    word= input("enter word: ")
    if word.lower() == "c":
        break
    elif word.isalpha():
        if len(word) > len(longest_word):
            longest_word = word
    else:
        print("you didn't enter word")

    print(longest_word)


