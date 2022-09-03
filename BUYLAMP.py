# cook your dish here
for _ in range(int(input())):
    n,k,x,y=map(int,input().split())
    if ((k*x+(n-k)*y)<n*x):
        print(k*x+(n-k)*y)
    else:
        print(n*x)