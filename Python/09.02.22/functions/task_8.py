#!/usr/bin/python3
def upper(mstr):
    nmstr = ""
    title_mstr = mstr.split()
    for i in range(len(title_mstr)):
        nmstr += title_mstr[i -1] + " "
    return nmstr
def main():
    mstr = input("enter string: ")
    print(upper(mstr))
if __name__ == "__main__":
    main()
