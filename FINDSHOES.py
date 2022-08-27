# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    
    if(m>=n):
        print(n)
    else:
        print(n+(n-m))