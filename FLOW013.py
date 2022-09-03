# cook your dish here
for i in range(int(input())):
    l=list(map(int,input().split()))
    if(sum(l)==180):
        print("YES")
    else:
        print("NO")