#!/usr/bin/python3
def lines(ml):
    return len(ml)
def main():
    ml = []
    print("if you want break input enter 'c'")
    while True:
        arg = input("enter somethin:  ")
        if arg == "c":
            print(lines(ml))
            break
        else:
            ml.append(arg)
if __name__ == "__main__":
    main()


