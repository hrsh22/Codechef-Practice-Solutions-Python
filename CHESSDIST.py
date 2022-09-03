# cook your dish here
for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    cd = max(abs(x1-x2),abs(y1-y2))
    print(cd)