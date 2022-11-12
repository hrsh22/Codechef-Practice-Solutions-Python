# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    count=0
    
    for i in range(1,n):
        if s[i-1]==s[i]:
                count+=1
    print(count)