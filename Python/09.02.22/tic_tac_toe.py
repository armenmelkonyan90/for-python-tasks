#!/usr/bin/python3
import random
def get_scheme(matrix=[" ", " "," "," "," "," "," "," "," "]):
    print("-------------")
    print("| "+matrix[0]+" | "+matrix[1]+" | "+matrix[2]+" |")
    print("-------------")
    print("| "+matrix[3]+" | "+matrix[4]+" | "+matrix[5]+" |")
    print("-------------")
    print("| "+ matrix[6] +" | "+matrix[7]+" | "+matrix[8]+" |")
    print("-------------")
    return matrix
def write_in_scheme(matrix,xo):
    while True:
        cell_num = input("In wich cell put a <"+xo+"> ? ")
        if cell_num.lower() == "c":
            exit()
        if cell_num.isdigit() and int(cell_num) >= 1 and int(cell_num) <= 9:
            if matrix[int(cell_num)-1] not in 'XO':
                matrix[int(cell_num)-1] = xo
                break
            else:
                print("This cell is not empty")
                continue
        else:
             print("incorrect input. enter the number 1-9")
             continue
    get_scheme(matrix)
    return matrix
def cpu_step(matrix, xo):
    while True:
        cell_num = random.randint(1, 9)
        if matrix[cell_num-1] == " ":
            matrix[cell_num -1] = xo
            break
    get_scheme(matrix)
    return matrix
def how_to_win(matrix):
    flag=False
    if matrix[0] == matrix[1] == matrix[2] != " " or matrix[3] == matrix[4] == matrix[5] != " " or matrix[6] == matrix[7] == matrix[8] != " " or matrix[0] == matrix[3] == matrix[6] != " " or matrix[1] == matrix[4] == matrix[7] != " " or matrix[2] == matrix[5] == matrix[8] != " " or matrix[0] == matrix[4] == matrix[8] != " " or matrix[2] == matrix[4] == matrix[6] != " ":
       flag=True
    return flag
def two_players_game():
        cnt = 0
        gs = get_scheme()
        while True:
            if cnt % 2 == 0:
                wis=write_in_scheme(gs,"X")
            else:
                write_in_scheme(gs,"O")
            cnt += 1
            if cnt > 4:
                chek = how_to_win(wis)
                if chek:
                    if cnt%2 == 0:
                        print("      !!!!! >O< IS WIN!!! !!!!")
                        get_scheme()
                        break
                    else:
                        print("      !!!!! >X< IS WIN!!! !!!!")
                        get_scheme()
                        break
            if cnt == 9:
                print(" Game Ower!! nobody won")
                break
def first_cpu():
    cnt=0
    gs=get_scheme()
    while True:
        cs=cpu_step(gs, "O")
        cnt+=1
        if cnt>8:
            print(" Game Ower!! nobody won")
            break
        if cnt>4:
            if how_to_win(cs):
                print("   !!!!!  >CPU< IS  WIN!!!  !!!!!")
                get_scheme()
                break
        wis=write_in_scheme(gs, "X")
        cnt+=1
        if cnt>4:
            if how_to_win(wis):
                print("     !!!!! YOU WIN!!!  !!!!!")
                get_scheme()
                break
def first_human():
    cnt=0
    gs=get_scheme()
    while True:
        wis=write_in_scheme(gs, "X")
        cnt+=1
        if cnt>8:
            print(" Game Ower!! nobody won")
            break
        if cnt>4:
            if how_to_win(wis):
                print("     !!!!! YOU WIN!!!  !!!!!")
                get_scheme()
                break
        cs=cpu_step(gs, "O")
        cnt+=1
        if cnt>4:
            if how_to_win(cs):
                print("     !!!!! >CPU< IS  WIN!!!  !!!!!")
                get_scheme()
                break
def main():
    print("    WELCOM TO TIC-TAC-TOE GAME. \n      Instructions \n write the number of the cell where you want to put a cross or a zero. \n cells are numbered from right to left and top to bottom \n 1 2 3 \n 4 5 6 \n 7 8 9 \n ------------------------------\n to exit the game enter 'c'")
    while True:
        var = input(" GAME OPTIONS:  1 player(with computer) - enter < 1 > \n                2 player                - enter < 2 >\n ")
        if var.lower() == "c":
            exit()
        elif var not in '12':
            print("  !!!Incorrect game option!!!")
        else:
            break
    if var == "1":
        while True:
            first_gamer = input(" WHO STARTS? enter < I > or <CPU >\n ")
            if first_gamer.lower() == "i":
                first_human()
                break
            elif first_gamer.lower() == "cpu":
                first_cpu()
                break
            elif first_gamer.lower() == "c":
                exit()
            else:
                print("incorrect input try again")
                continue
    if var == "2":
        two_players_game()
if __name__ == "__main__":
    main()

