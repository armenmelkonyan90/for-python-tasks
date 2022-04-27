#!/usr/bin/python3
def get_list_nums(mstr):
    ml=mstr.split()
    nml=[]
    for el in ml:
        if str(el).isdigit():
            nml.append(el)
    print(nml)
    return nml
def sort_list(nml):
    nml = sorted(nml, reverse=True)
    return nml[0]
def main():
    mstr = input("enter list ")
    gln = get_list_nums(mstr)
    print(sort_list(gln))
if __name__ == "__main__":
    main()
