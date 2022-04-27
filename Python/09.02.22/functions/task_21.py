#!/usr/bin/python3
def numbers_in_list(ml):
    ave=0
    cnt=0
    for el in ml:
        if str(el).isdigit():
            ave += int(el)
            cnt +=1
    return (ave/cnt)
def main():
    ml = ["32", "saa", 43, 65, "e", "/>", 9, 23]
    print(numbers_in_list(ml))
if __name__ == "__main__":
    main()
