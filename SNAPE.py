# cook your dish here
import math
for _ in range(int(input())):
    b,ls=map(int,input().split())
    print(math.sqrt(ls**2-b**2),math.sqrt(ls**2+b**2))