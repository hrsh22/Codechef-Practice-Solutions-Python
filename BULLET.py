# cook your dish here
for _ in range(int(input())):
    x,y,z = map(int,input().split())
    frames = y//x
    mintime = z - frames
    if(mintime>0):
        print(mintime)
    else:
        print(0)