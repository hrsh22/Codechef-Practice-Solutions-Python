# cook your dish here
import math
for _ in range(int(input())):
    l,k=map(int,input().split())
    
    if l%k==0:
        print(0)
    else:
        print(math.ceil(l/k)-(l//k))