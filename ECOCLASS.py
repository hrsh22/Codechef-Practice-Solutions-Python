# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    z=0
    for i in range(n):
        if a[i]==b[i]:
            z+=1
    print(z)