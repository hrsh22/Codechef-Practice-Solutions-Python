# cook your dish here
for _ in range(int(input())):
    vowel=['a','e','i','o','u']
    n=int(input())
    s=input()
    count=0
    for i in s:
        if i in vowel:
           count=0
        else:
            count+=1
            if count==4:
                break
    if count==4:
        print('no')
    else:
        print('yes')