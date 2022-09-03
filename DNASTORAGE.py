# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()[:n]
    z=''
    for i in range(0,n-1,2):
        if(s[i]+s[i+1]=='00'):
            z+='A'
        if(s[i]+s[i+1]=='01'):
            z+='T'
        if(s[i]+s[i+1]=='10'):
            z+='C'
        if(s[i]+s[i+1]=='11'):
            z+='G'
    print(z)