# cook your dish here
for _ in range(int(input())):
    l=int(input())
    a=input()
    b=a.replace('.','')
    b=b.replace('HT','')
    if b=='':
        print('Valid')
    else:
        print('Invalid')