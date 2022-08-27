# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if(x%3==0):
        print('Normal')
    elif(x%3==1):
        print('Huge')
    else:
        print('Small')