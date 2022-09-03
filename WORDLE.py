# cook your dish here
for _ in range(int(input())):
    s=input()
    t=input()
    z=''
    for i in range(5):
        if s[i]==t[i]:
            z+='G'
        else:
            z+='B'
    print(z)