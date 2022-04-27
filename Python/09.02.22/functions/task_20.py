#!/usr/bin/python3
def even_duble(ml):
    nml = []
    for el in ml:
        if str(el).isdigit() and len(str(el)) == 2 and int(el) % 2==0:
            nml.append(el)
    return nml
def main():
    ml = ["2", "24", 25, "ds", "66", 100, "65", "72"]
    print(even_duble(ml))
if __name__ == "__main__":
    main()
