# cook your dish here
for _ in range(int(input())):
    char=str(input())
    if char is 'B' or char is 'b':
        print("BattleShip")
    elif char is 'C' or char is 'c':
        print("Cruiser")
    elif char is 'D' or char is 'd':
        print("Destroyer")
    elif char is 'F' or char is 'f':
        print("Frigate")