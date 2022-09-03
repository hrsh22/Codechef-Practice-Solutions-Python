# cook your dish here
r,o,c = map(int,input().split())
rem = r-c
if (rem>=36*(20-o)):
    print("no")
else:
    print("yes")