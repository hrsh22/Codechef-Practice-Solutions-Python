# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    if n%3==0:
        print(2*x*(n//3))
    else:
        print(2*x*(n//3)+x*(n%3))