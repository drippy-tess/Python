print("Adja meg a kezdő értéket!")
kezdoErtek: int = int(input())

print("Adja meg a végértéket!")
vegErtek: int = int(input())

for i in range(vegErtek, kezdoErtek, -1):
    print(i)