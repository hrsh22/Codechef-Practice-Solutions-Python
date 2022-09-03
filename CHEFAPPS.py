# cook your dish here
for _ in range(int(input())):
    s,x,y,z = map(int,input().split())
    avl = s-(x+y)
    if(z<=avl):
        print(0)
    elif(z<=avl+x or z<=avl+y):
        print(1)
    else:
        print(2)