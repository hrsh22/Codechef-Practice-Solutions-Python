# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    
    if((n/m)%2==0):
        print('yes')
    else:
        print('no')