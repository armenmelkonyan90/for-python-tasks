#!/bin/python3
nds = [2,44,34,5,-2,5,77,8,91,-4,15,23,-8,21, -19]
#task 1
def task_1():
    count = 0
    for i in range(len(nds)):
        if nds[i] < int(i)**2:
            count += 1
    print(count, "elements from the list are less than the square of their number")
def task_2():
    ave = 0
    ml = []
    for i in nds:
        ave += int(i)
    ave = ave/len(nds)
    for i in nds:
        ml.append(ave-int(i))
    print(ml)
def task_3():
    count = 0
    for i in range(len(nds)-1):
        if nds[i] < (nds[i-1] + nds[i+1])/2:
            count += 1
    print(count, "elements that are less than half the sum of the previous and next elements")
def task_4():
    el = max(nds)
    pas = 0
    for i in range(len(nds)):
        if nds[i] == el:
            pas = i
   
    print(pas,"-th element in the list is maximum and equal", el)
def task_5():
    maxval=max(nds)
    minval=min(nds)
    diff = maxval-minval
    print("difference between the maximum and minimum elements of a list: ",diff)
def task_6():
    count = 0
    maxval=0
    minval=0
    for i in range(len(nds)):
        if nds[i] == max(nds):
            maxval = i
        if nds[i] == min(nds):
            minval = i
    for i in range(minval, maxval):
        count += nds[i]
    print("the sum of the elements between the maximum and minimum elements is",count)
def task_7():
    count=0
    n=1
    while n<len(nds):
        for i in range(len(nds)-n):
            if nds[i] < nds[i+1]:
                nds[i],nds[i+1] = nds[i+1],nds[i]
        n+=1
    count = int(nds[0]) + int(nds[1])
    print("the sum of the largest and second largest elements is ", count)
def task_8():
    if max(nds) <  0:
        print("the list does not contain positive numbers")
    else:
        n=1
        while n<len(nds):
            for i in range(len(nds)-n):
                if nds[i] > nds[i+1]:
                    nds[i],nds[i+1] = nds[i+1],nds[i]
            n+=1
        for i in nds:
            if i>0:
                print("smallest positive number in the list is",i)
                break


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
if __name__ == "__main__":
    main()
