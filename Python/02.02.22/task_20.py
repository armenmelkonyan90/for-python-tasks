#!/bin/python3
matrix=[]
def def_matrix(n):
   # matrix = []
    for i in range(int(n)):
        i_array = []
        for j in range(int(n)):
            i_array.append(2*i+j)
        matrix.append(i_array)
        print(i_array)
    return matrix
def sum_elements():
    print("task 20a")
    summ=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            summ += matrix[i][j]
    print("sum of all matrix elements is ",summ)

def sum_rows_elements():
    print("task 20b")
    summ=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            summ+=matrix[i][j]
        print("the sum of the elements of the ",i,"row is ",summ)
        summ = 0
def greater_5():
    cnt = 0
    swich = False
    print("task 20c")
    for i in range(len(matrix)):
        for j in range(len( matrix[i])):
            if int(matrix[i][j]) > 5:
                swich = True
            else:
                break
        if swich == True:
            cnt+=1
    print("in the ",cnt,"rows of the matrix, all elements are greater than five")
def diff_elements():
    count=0
    swich = False
    print("task 20d")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            if matrix[i][j] != matrix[i][j+1]:
                swich = True
            else:
                break
        if swich:
            count+=1
    print("in the",count,"rows of the matrix, all elements are different")
def sum_of_elements_greater_5():
    swich = False
    summ=0
    print("task 20e")
    for i in range(len(matrix)):
        for j in range(len( matrix[i])):
            if int(matrix[i][j]) > 5:
                swich = True
                summ += matrix[i][j]
            else:
                swich = False
                summ = 0
                break
        if swich == True:
            print(" all elements of the ",i,"-th row are greater than 5. the sum of these elements is", summ)
        summ = 0
def max_of_mins():
    min_list = []
    print("task 20f")
    for i in range(len(matrix)):
        min_list.append(min(matrix[i]))
    max_min = max(min_list)
    print("max value of min elements of the rows of the matrix is ",max_min)




def main():
    n = input("enter the length of the matrix")
    if n.isdigit():
        def_matrix(n)
        sum_elements()
        sum_rows_elements()
        greater_5()
        diff_elements()
        sum_of_elements_greater_5()
        max_of_mins()
    else:
        print("enter only number")



if __name__ == "__main__":
    main()
