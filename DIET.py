# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    a=list(map(int,input().split()))
    z=0
    for i in range(len(a)):
        z+=a[i]
        z-=k
        if z<0:
            print('NO',i+1)
            break
    if z>=0:
        print('YES')