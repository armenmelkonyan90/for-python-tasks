#!/bin/python3
def my_replace(mstr, word, new_word):
    new_mstr = ""
    if len(word) == 1:
        for i in mstr:
            if i == word:
                new_mstr += new_word
            else:
                new_mstr += i
    else:
        nmstr = mstr.split()
        for i in range(len(nmstr)):
            if nmstr[i] == word:
                new_mstr += new_word +" "
            else:
                new_mstr += nmstr[i] + " "
    return new_mstr
print(my_replace("london is a capital of great britain", "capital", "city"))
