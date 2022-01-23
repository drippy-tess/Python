print("x= ")
x: int = int(input())

print("y= ")
y: int = int(input())

if (y % x == 0):
    print(f"{y} osztható {x}.")
else:
    print(f"{y} nem osztható {x}.")