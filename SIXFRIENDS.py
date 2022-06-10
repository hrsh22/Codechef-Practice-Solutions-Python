# cook your dish here
T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    if 3*X>2*Y:
        print(2*Y)
    else:
        print(3*X)