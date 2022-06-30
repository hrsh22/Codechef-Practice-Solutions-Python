# cook your dish here
for _ in range(int(input())):
    x,a,b=map(int,input().split())
    total=a+2*b
    if(total>=x):
        print("qualify")
    else:
        print("notqualify")