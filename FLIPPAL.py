# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    OneCount=s.count('1')
    ZeroCount=s.count('0')
    
    if OneCount%2!=0 and ZeroCount%2!=0:
        print('No')
    else:
        print('Yes')