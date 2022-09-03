# cook your dish here
for _ in range(int(input())):
    m,n,k=map(int,input().split())
    if n*k<m:
        print('yes')
    else:
        print('no')