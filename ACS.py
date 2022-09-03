# cook your dish here
for _ in range(int(input())):
    p=int(input())
    if p//100 + p%100 <=10:
        print(p//100 + p%100)
    else:
        print(-1)