print("x= ")
x: int = int(input())

if (x >= 0 and x <= 9):
    print(f"{x} egyjegyű.")
elif (x >= 10 and x <= 99):
    print(f"{x} kétjegyű.")
elif (x >= 100 and x<= 999):
    print(f"{x} háromjegyű.")
else:
    print(f"{x} négy vagy többjegyű.")