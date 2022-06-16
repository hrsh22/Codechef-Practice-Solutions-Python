# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    max=(z-y)//x
    print(max)