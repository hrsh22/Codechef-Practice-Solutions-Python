# cook your dish here
for _ in range(int(input())):
    a,b,c,p,q,r=map(int,input().split())
    reqVotes = (p+q+r)/2
    if (p+b+c)>reqVotes or (a+q+c)>reqVotes or (a+b+r)>reqVotes:
        print("YES")
    else:
        print("NO")