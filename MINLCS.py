# cook your dish here
for _ in range(int(input())):
    n=int(input())
    A=list(input())
    B=list(input())
    CountA={}
    CountB={}
    z=[0]
    
    for i in A:
        if i in CountA:
            CountA[i]+=1
        else:
            CountA[i]=1

    for i in B:
        if i in CountB:
            CountB[i]+=1
        else:
            CountB[i]=1
    
    for i in CountA.keys():
        if i in CountB.keys():
            minC = min(CountA[i],CountB[i])
            z.append(minC)
    print(max(z))