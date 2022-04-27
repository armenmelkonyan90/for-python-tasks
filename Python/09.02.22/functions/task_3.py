#!/usr/bin/python3
def res(ml):
    result = 0
    cnt = 0
    ave = 0
    if len(ml) == 0:
        return 0
    for el in ml:
        result += int(el)
        cnt +=1
    ave = result/cnt
    return ave
def main():
    ml = []
    print("if you want break input enter 'c'")
    while True:
        arg = input("enter somethin:  ")
        if arg == "c":
            print(ml)
            print("Arithmetic mean of entered numbers is", res(ml))
            break
        if arg.isdigit():
            ml.append(arg)
        else:
            print("enter only numbers please")
if __name__ == "__main__":
    main()


