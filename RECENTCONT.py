# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(input().split())
    s=0
    for i in a:
        if i=='START38':
           s+=1
    print(s, end=' ')
    print(n-s)