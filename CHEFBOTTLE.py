# cook your dish here
for _ in range(int(input())):
    n,x,k = map(int,input().split())
    maxnum = int(k/x)
    
    if(maxnum>n):
        print(n)
    else:
        print(maxnum)