# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    decimal=int(s,2)
    temp = 0
    a=[]

    for i in range(1,n+1):
        temp = decimal^(decimal>>i)
        a.append(temp)
    index = a.index(min(a))
    print(index+1)