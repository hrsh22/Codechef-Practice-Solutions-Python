# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    total=5*x+10*y
    maxch=total//z
    print(maxch)