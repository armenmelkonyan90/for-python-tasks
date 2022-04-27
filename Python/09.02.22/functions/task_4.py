#!/usr/bin/python3
def math_operations(a,b):
#    dict_ = {}
#    dict_["summ"] = a+b
#    dict_["diff"] = a-b
#    dict_["mult"] = a*b
#    dict_["div"] = a/b
#    return dict_
#     ---OR--
    summ = a+b
    diff = a-b
    mult = a*b
    div = a/b
    return summ,diff,mult,div
def main():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(math_operations(a,b))
if __name__ == "__main__":
    main()
