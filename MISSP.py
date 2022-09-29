# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    for i in a:
        if a.count(i)%2!=0:
            print(i)
            break