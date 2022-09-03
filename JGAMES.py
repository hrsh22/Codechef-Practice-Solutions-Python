# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    
    if x%2==0 and y%2!=0:
        print('jay')
    elif x%2==0 and y%2==0:
        print('janmansh')
    elif x%2!=0 and y%2==0:
        print('jay')
    else:
        print('janmansh')