# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    if n%2==1:
        if x%2==1:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')