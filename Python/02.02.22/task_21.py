#!/bin/python3
matrix=[]
def creat_matrix(n):
    for i in range(int(n)):
        i_array = []
        for j in range(int(n)):
            if (i+j) % 2 == 0:
                i_array.append(2*i+2*j+int(n))
            else:
                i_array.append(2*i+2*j*int(n)*-1)
        matrix.append(i_array)
        print(i_array)
    return matrix
def neg_els():
    count=0
    neg_cnt = []
    print("task 21a")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] <0:
                count+=1
        neg_cnt.append(count)
        count = 0
    print("list for negativ elements count in the rows is--- ",neg_cnt)
def pos_even_el():
    summ=0
    pos_el=[]
    print("task 21b")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0 and matrix[i][j] % 2 == 0:
                summ+=matrix[i][j]
        pos_el.append(summ)
        summ=0
    print("list of sums of positive even numbers is ", pos_el)
def mult_g0():
    mult=1
    zero=0
    mult_el = []
    print("task 21c")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0 and matrix[i][j] <10:
                mult *=matrix[i][j]
            if matrix[i][j] < 0 and matrix[i][j] > -10:
                mult *= matrix[i][j]
            if matrix[i][j] > 10 or matrix[i][j] < -10:
                for el in range(matrix[i][j]):
                    if el == 0:
                        continue
                else:
                    mult *= matrix[i][j]
        if mult ==1:
            mult_el.append(zero)
        else:
            mult_el.append(mult)
        mult = 1
    print("list of not zero numbers multiply is: ", mult_el)
def eq_1():
    count = 0
    eq_1_list = []
    print("task 21d")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(str(matrix[i][j]))):
                if int(k) == 3:
                    count +=1
                    continue
        if count == len(matrix[i]):
            eq_1_list.append(1)
        else:
            eq_1_list.append(-1)
    print("1 or -1 list -  ",eq_1_list)
def ave_column():
    ave = 0
    summ = 0
    ave_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            summ += matrix[j][i]
        ave = summ/len(matrix[i])
        ave_list.append(ave)
        summ = 0
        ave = 0
    print("columns avereges list is ", ave_list)
            

                


def main():
    n = input("enter n ")
    if n.isdigit():
        creat_matrix(n)
        neg_els()
        pos_even_el()
        mult_g0()
        eq_1()
        ave_column()

    else:
        print("enter only number")

if __name__ == "__main__":
    main()
