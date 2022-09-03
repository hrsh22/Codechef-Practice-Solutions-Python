# cook your dish here
for _ in range(int(input())):
    n,x,y,a,b=map(int,input().split())
    if (n/a)*x<(n/b)*y:
        print('petrol')
    elif (n/a)*x>(n/b)*y:
        print('diesel')
    else:
        print('any')