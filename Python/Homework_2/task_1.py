#!/bin/python3
for i in range(100, 998, 2):
    if (int(i / 10) % 10 == 0 and i % 10 != 4):
        print(i)

