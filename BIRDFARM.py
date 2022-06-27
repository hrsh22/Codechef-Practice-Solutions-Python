# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if (z%x==0 and z%y==0):
        print("any")
    elif(z%x==0):
        print("chicken")
    elif(z%y==0):
        print("duck")
    else:
        print("none")
    