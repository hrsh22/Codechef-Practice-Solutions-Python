# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    z=x*n-sum(a)
    if z<0:
        print(0)
    else:
        print(z)