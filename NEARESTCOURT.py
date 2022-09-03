# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    s=int((x+y)/2)
    print(max(abs(x-s),abs(y-s)))