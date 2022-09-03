# cook your dish here
for _ in range(int(input())):
    n=int(input())
    flag=False
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
    if flag==True:
        print('no')
    elif n==1:
        print('no')
    else:
        print('yes')