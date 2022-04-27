#!/usr/bin/python3
def sum_of_nums(num):
    res=int(num[0])*int(num[-1])
    return res
def main():
    num=input("Enter a number greater than 9 ")
    if len(num) == 0 or num.isalpha() or num in '/.,?><";:\][|}{=-+_)(*&^%$@!~`':
        print("Enter a number greater than 9")
    else:
        print("The multiply of first and last digits is ",sum_of_nums(num))
if __name__ == "__main__":
    main()

