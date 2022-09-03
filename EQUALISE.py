# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a 
    while a<b:
        a*=2
    print("yes" if a==b else "no")