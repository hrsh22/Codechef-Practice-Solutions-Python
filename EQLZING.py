# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if((a+b)%2==0):
        print('yes')
    else:
        print('no')