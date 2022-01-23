eredmeny: int = 0

print("Kezdő Érték: ")
kezdoErtek: int = int(input())

print("Vég Érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek +1, 1):
    if(i % 2 != 0 and i % 3 == 0):
        eredmeny += 1

print(f"{eredmeny}")