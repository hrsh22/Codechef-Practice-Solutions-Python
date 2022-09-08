# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        print('1',end='')
        print((n-2)*'0',end='')
        print('1')
    else:
        print('0',end='')
        print((n-2)*'1',end='')
        print('0')