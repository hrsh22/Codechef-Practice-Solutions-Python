# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    z=0
    for i in range(len(lst)):
        if lst[i]>=10 and lst[i]<=60:
            z+=1
    print(z)
    