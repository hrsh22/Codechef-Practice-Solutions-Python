# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    if ((x-w)>(y*z)):
        print("unfilled")
    elif ((x-w)==(y*z)):
        print("filled")
    else:
        print("overflow")