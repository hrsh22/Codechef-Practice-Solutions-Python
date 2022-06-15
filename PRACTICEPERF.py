# cook your dish here
p=list(map(int,input().split()))
s=0
for a in p:
    if a>=10:
        s+=1
print(s)