# cook your dish here
for _ in range(int(input())):
    sx,sy,ex,ey = map(int,input().split())
    if(sx==ex or sy==ey):
        print(2)
    else:
        print(1)