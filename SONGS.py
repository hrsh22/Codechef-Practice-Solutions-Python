# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    
    if(n>=3*x):
        print(n//(3*x))
    else:
        print("0")
        