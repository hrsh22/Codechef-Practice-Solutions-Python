# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    a=(x-1)//10
    b=(y-1)//10
    print(abs(a-b))