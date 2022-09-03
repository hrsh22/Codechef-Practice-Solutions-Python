# cook your dish here
for _ in range(int(input())):
    xa,xb,Xa,Xb = map(int,input().split())
    a=0
    b=0
    if Xa%xa==0:
        a=Xa//xa
    else:
        a=(Xa//xa)+1
    if Xb%xb==0:
        b=Xb//xb
    else:
        b=(Xb//xb)+1
    print(a+b)
    