# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    if(x/100*107)>=y:
        print("YES")
    else:
        print("NO")