#!/usr/bin/python3
def res(ml):
    result = 0
    for el in ml:
            result += int(el)
    return result
def main():
    ml = []
    print("if you want break input enter 'c'")
    while True:
        arg = input("enter somethin:  ")
        if arg == "c":
            print(ml)
            print(res(ml))
            break
        if arg.isdigit():
            ml.append(arg)
if __name__ == "__main__":
    main()

