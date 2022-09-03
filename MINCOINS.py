# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if(x%10==0):
        print(x//10)
    elif(x%5==0):
        a=x//10
        print(a+(x%10)//5)
    else:
        print(-1)