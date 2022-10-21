# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    maxI=0
    Rmax=0
    choice=0
    for i in range(n):
        if l[i]*r[i]>maxI:
            maxI=l[i]*r[i]
            Rmax=r[i]
            choice=i+1
        elif l[i]*r[i]==maxI and r[i]>Rmax:
                Rmax=r[i]
                choice=i+1
    print(choice)
                