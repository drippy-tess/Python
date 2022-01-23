print("x= ")
x: int = int (input())

if (10 < x < 20):
    print(f"{x} 10 és 20 között lévő szám.")
else:
    print(f"{x} nincs 10 és 20 között.")

if (-10 > x > -20):
    print(f"{x} -10 és -20 között van.")
else: 
    print(f"{x} nincs -10 és -20 között.")