# cook your dish here
for _ in range(int(input())):
    n=list(map(int,input().split()))
    n.remove(len(n)-1)
    print(max(n))