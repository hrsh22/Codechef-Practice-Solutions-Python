# cook your dish here
for _ in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    minDist=abs(c-a)+abs(d-b)
    if minDist%2==0:
        if minDist<=k and k%2==0:
            print("Yes")
        else:
            print("No")
    else:
        if minDist<=k and k%2!=0:
            print("Yes")
        else:
            print("No")