# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    if y>x:
        print("bike")
    elif x>y:
        print("car")
    else:
        print("same")
        