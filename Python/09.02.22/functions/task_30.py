#!/usr/bin/python3
def sort_by_length(d_list):
    n=1
    while n<len(d_list):
        for i in range(len(d_list)-n):
            if len(d_list[i]["university"]) < len(d_list[i+1]["university"]):
                d_list[i],d_list[i+1] = d_list[i+1],d_list[i]

        n += 1
    return d_list[0]
def main():
    d_list = [{"university": "Yerevan State University"},
              {"university": "American University of Armenia"},
              {"university": "Armenian National Agrarian University"},
              {"university": "Russian-Armenian University"},
              {"university": "Armenian State University of Economics"},
              {"university": "asysas"}]
    print(sort_by_length(d_list))
if __name__ == "__main__":
    main()
