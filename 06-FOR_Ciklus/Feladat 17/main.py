atlag: float = 0
szamokSzama: int = 0
szamokOsszeg: int = 0

print("Kezdő érték= ")
kezdoErtek: int = int(input())

print("Vég érték= ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    szamokOsszeg += 1
    szamokSzama += i

atlag = szamokSzama / szamokOsszeg

print(f"{atlag}")