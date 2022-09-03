# cook your dish here
for _ in range(int(input())):
    x,y,a,b=map(int,input().split())
    z=0
    if x!=a and x!=b:
        z+=1
    if y!=a and y!=b:
        z+=1
    print(z)