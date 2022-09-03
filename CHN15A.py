# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    z=0
    lst=list(map(int,input().split()))
    for j in lst:
        if((j+k)%7==0):
            z+=1
    print(z)