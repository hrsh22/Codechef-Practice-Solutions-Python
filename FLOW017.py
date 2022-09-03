# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    l=[a,b,c]
    l.sort()
    print(l[1])
    