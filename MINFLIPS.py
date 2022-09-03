# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    z=a.count(1)
    if(n%2!=0):
        print(-1)
    else:
        print(abs(z-(n//2)))
    