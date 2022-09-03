# cook your dish here
for _ in range(int(input())):
    x,m,d=map(int,input().split())
    delay=m*x-x
    if delay>d:
        print(d+x)
    else:
        print(m*x)
    