# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if z*2>=(y-x):
        print('yes')
    else:
        print('no')