# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    if(n==x):
        print("yes")
    elif(x%n==0):
        print("yes")
    else:
        print("no")