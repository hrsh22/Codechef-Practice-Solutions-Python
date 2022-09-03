# cook your dish here
for _ in range(int(input())):
    sa,sb,sc=map(int,input().split())
    z=min(sa,sb,sc)
    if sc==z:
        print('Alice')
    elif sb==z:
        print('Bob')
    else:
        print('Draw')