# cook your dish here
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    if x*y>=a*b:
        print("yes")
    else:
        print("no")