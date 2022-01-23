print("x= ")
x: int = int(input())

print("y= ")
y: int = int(input())

if (x > y):
    print(f"{y}, {x}")
elif (y > x):
    print(f"{x}, {y}")
else:
    print(f"{x} = {y}")