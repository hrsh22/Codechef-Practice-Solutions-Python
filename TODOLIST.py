# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))[:n]
    z=0
    for i in lst:
        if i>=1000:
            z+=1
    print(z)