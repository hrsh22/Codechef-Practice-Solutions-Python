# cook your dish here
for _ in range(int(input())):
    p,q = map(int,input().split())
    x=(p+q)//2
    if(x%2==0):
        print('Alice')
    else:
        print('Bob')