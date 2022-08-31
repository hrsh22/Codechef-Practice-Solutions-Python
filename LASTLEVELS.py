# cook your dish here
for _ in range(int(input())):
    x,y,z = map(int,input().split())
    t = x*y
    if x>3 and x%3!=0:
        t += ((x//3) *z)
    elif x>3:
        t += (((x//3)-1) *z)
    print(t)