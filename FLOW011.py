# cook your dish here
for _ in range(int(input())):
    sal=int(input())
    if sal<1500:
        print(sal+(10/100)*sal+(90/100)*sal)
    else:
        print(sal+500+(98/100)*sal)