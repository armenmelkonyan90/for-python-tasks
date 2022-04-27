#!/usr/bin/python3
def sort_with_ages(d_list):
    n=1
    while n<len(d_list):
        for i in range(len(d_list)-n):
            if d_list[i]["age"] < d_list[i+1]["age"]:
                d_list[i],d_list[i+1] = d_list[i+1],d_list[i]
        n+=1
    return d_list[0]

def main():
    d_list = [{"name": "Jhon", "age": 34, "height": 172},
              {"name": "Jhon", "age": 37, "height": 176},
              {"name": "Jhon", "age": 49, "height": 181},
              {"name": "Jhon", "age": 38, "height": 168}]
    print(sort_with_ages(d_list))
if __name__ == "__main__":
    main()
