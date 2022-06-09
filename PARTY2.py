# cook your dish here
T=int(input())
for _ in range(T):
    N,X,K=map(int,input().split())
    if K/X>=N:
        print("YES")
    else:
        print("NO")