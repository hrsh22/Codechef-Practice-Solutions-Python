# cook your dish here
for _ in range(int(input())):
    d=int(input())
    s=input()
    count=0
    prox=0
    for i in range(d):
        if i<=1 or i>=d-2:
            if s[i]=='P':
                count+=1
        elif s[i]=='P':
            count+=1
        elif (s[i-2]=='P' or s[i-1]=='P') and (s[i+1]=='P' or s[i+2]=='P'):
            prox+=1
    if (count/d)>=0.75:
        print(0)
    elif (prox+count)/d>=0.75:
        j=1
        while (count+j)/d<0.75:
            j+=1
        print(j)
    else:
        print(-1)