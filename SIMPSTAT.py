# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=sorted(list(map(int,input().split())))[k:n-k]
    avg="{0:.6f}".format(sum(a)/len(a))
    print(avg)