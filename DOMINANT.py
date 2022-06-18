# cook your dish here
for _ in range(int(input())):
    Na,Nb,Nc=map(int,input().split())
    if(Na>Nb+Nc) or (Nb>Na+Nc) or (Nc>Na+Nb):
        print("YES")
    else:
        print("NO")