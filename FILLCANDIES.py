# cook your dish here
import math
for _ in range(int(input())):
    n,k,m=map(int,input().split())
    maxcan = n/(k*m)
    print(math.ceil(maxcan))