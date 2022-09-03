# cook your dish here
from math import ceil
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x == y:
        print(0)
    elif x < y:
        print(y - x)
    else:
        if (x - y) % 2 == 0:
            print((x - y) // 2)
        else:
            print(ceil((x - y) / 2) + 1)