# cook your dish here
import math
for _ in range(int(input())):
    n,x=map(int,input().split())
    print(math.ceil((n*x)/4))