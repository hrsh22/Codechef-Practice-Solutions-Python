# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    
    if (a%2==0 or b%2==0 or c%2==0) and (a%2!=0 or b%2!=0 or c%2!=0):
        print("yes")
    else:
        print("no")