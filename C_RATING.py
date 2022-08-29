# cook your dish here
for _ in range(int(input())):
    x,y = map(int,input().split())
    i=0
    while(x<y):
        x=x+8
        i=i+1
    print(i)