# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    count=0
    while(n>=k):
        n-=k
        count+=1
    print(count*count)