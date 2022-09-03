# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    
    time_A = abs((x*2)-500)
    time_B = abs((x+y)*4-1000)
    time1_A = abs((x+y)*2-500)
    time1_B = abs((y*4)-1000)
    
    total1 = time_A + time_B
    total2 = time1_A + time1_B
    
    print(max(total1,total2))