# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for i in reversed(range(n)):
        if a[i]!=0:
            print(i)
            break