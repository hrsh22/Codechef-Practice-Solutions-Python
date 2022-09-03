# cook your dish here
for _ in range(int(input())):
    n=input()
    m=n[::-1]
    if n==m:
        print('wins')
    else:
        print('loses')