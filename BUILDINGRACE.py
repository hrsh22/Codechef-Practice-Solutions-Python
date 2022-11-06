# cook your dish here
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    chef=a/x
    chefina=b/y
    if chef>chefina:
        print("Chefina")
    elif chefina>chef:
        print("Chef")
    else:
        print("Both")