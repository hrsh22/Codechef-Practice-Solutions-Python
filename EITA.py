# cook your dish here
for _ in range(int(input())):
    d,x,y,z=map(int,input().split())
    a=7*x
    b=y*d+z*(7-d)
    print(max(a,b))