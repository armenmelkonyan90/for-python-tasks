#!/usr/bin/python3
def get_my_nums(ml):
    nml=[]
    for el in ml:
        if str(el).isdigit():
            nml.append(int(el))
    return nml
def sort_nml(nml):
    sml=[]
    sml = sorted(nml, reverse=True)
    return sml
def main():
    ml = ["43", 5, "t", 65, "88", "fdr", 90, "asa",61]
    #gmn = get_my_nums(ml)
    print(sort_nml(get_my_nums(ml)))
if __name__ == "__main__":
    main()
