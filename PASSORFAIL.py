# cook your dish here
for _ in range(int(input())):
    n,x,p=map(int,input().split())
    total = 3*x-(n-x)
    if total>=p:
        print("Pass")
    else:
        print("Fail")
    