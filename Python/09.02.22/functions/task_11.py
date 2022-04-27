#!/usr/bin/python3
def dict_for_letters(mstr):
    md = {}
    for el in mstr:
        if el == " " or el.isdigit():
            continue
        if el in md:
            md[el] +=1
        else:
            md[el] = 1
    return md
def get_most_used_letter(md):
    if len(md) == 0:
        return 0
    ml = []
    ml = sorted(md.items(), reverse=True, key=lambda x: x[1])
    return ml
def main():
    mstr = input("enter sentence ")
    dfl = dict_for_letters(mstr)
    ml=get_most_used_letter(dfl)
    if ml == 0:
        print("the sentence has no letters")
    else:
        print("most used letter in sentense is <",ml[0][0], ">. used ", ml[0][1], "time")
if __name__ == "__main__":
    main()

