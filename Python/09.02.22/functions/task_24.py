#!/usr/bin/python3
def sort_by_lenght(ml):
    new_ml=[]
    new_ml = sorted(ml, key=len, reverse=True)
    return new_ml
def main():
    ml = ["london", "is", "a", "capital", "of", "great", "britain"]
    print(sort_by_lenght(ml))
if __name__ == "__main__":
    main()
