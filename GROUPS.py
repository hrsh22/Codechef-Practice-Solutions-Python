# cook your dish here
for _ in range(int(input())):
    s=input()
    g=0
    for i in range(len(s)-1):
        if s[i]=='0' and s[i+1]=='1':
            g+=1
    if s[0]=='1':
        g+=1
    print(g)