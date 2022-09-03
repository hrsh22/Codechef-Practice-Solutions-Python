# cook your dish here
for _ in range(int(input())):
    w,x,y,z = map(int,input().split())
    if(w==x or w==x+y or w==x+z or w==x+y+z or w==y or w==y+z or w==z):
        print('yes')
    else:
        print('no')