parosOsszeg: int = 0
paratlanOsszeg: int = 0

print("Kezdő Érték: ")
kezdoErtek: int = int(input())

print("Vég Érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek +1, 1):
    if(i % 2 == 0):
        parosOsszeg += 1
    else:
        paratlanOsszeg += 1

if(paratlanOsszeg < parosOsszeg):
    print("A páros számok összege a nagyobb")
elif(parosOsszeg < paratlanOsszeg):
    print("A páratlan számok összege a nagyobb")
else:
    print("Egyenlőek")