# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a*10>b*5):
        print("first")
    elif(b*5>a*10):
        print("second")
    else:
        print("any")