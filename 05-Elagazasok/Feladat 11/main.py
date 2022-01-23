print("x= ")
x: int = int(input())

if (x % 2 == 0):
    print(f"{x} páros.")
else:
    print(f"{x} páratlan.")

if (x >= 0):
    print(f"{x} pozitív.")
else:
    print(f"{x} negatív.")

if (x % 5 == 0):
    print(f"{x} osztható 5-tel.")
else:
    print(f"{x} nem osztható 5-tel.")