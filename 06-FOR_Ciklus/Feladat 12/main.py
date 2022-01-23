harommalOszthatoSzamokSorozata: int = 0

print("Kezdő Érték: ")
kezdoErtek: int = int(input())

print("Vég Érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek +1, 1):
    if(i % 3 == 0):
        harommalOszthatoSzamokSorozata += 1

print(f"{harommalOszthatoSzamokSorozata}")