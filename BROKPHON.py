# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    if len(set(a))==1:
        print(0)
    else:
        for i in range(1,n-1):
            if a[i-1]!=a[i] or a[i]!=a[i+1]:
                count+=1
        if a[0]!=a[1]:
            count+=1
        if a[-2]!=a[-1]:
            count+=1
        print(count)
        