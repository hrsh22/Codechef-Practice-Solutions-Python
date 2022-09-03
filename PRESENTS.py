# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n%5==0:
        print(4*(n//5))
    else:
        print(4*(n//5)+n%5)