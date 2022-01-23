atlag: float = 0
parosSzamok: int = 0
paratlanSzamok: int = 0

print("Kezdő Érték: ")
kezdoErtek: int = int(input())

print("Vég Érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek +1, 1):
    if(i % 2 == 0):
        parosSzamok += i
    else:
        paratlanSzamok += i

atlag = (paratlanSzamok + parosSzamok) / 2

print(f"{atlag}")