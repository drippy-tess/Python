parosSzamokOsszege: int = 0
paratlanSzamokSzorzata: int = 1

print("Kezdő érték: ")
kezdoErtek: int = int (input())

print("Vég érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    if(i % 2 == 0):
        parosSzamokOsszege += i
    else:
        paratlanSzamokSzorzata *= i

print(f"A páros számok összege: {parosSzamokOsszege}.")
print(f"A páratlan számok szorzata: {paratlanSzamokSzorzata}.")