# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    z=''
    for i in range(len(a)):
        if k>=a[i]:
            k-=a[i]
            z+='1'
        else:
            z+='0'
    print(z)
        