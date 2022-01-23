ottelOszthato: int = 0
hettelOszthato: int = 0

print("Kezdő Érték: ")
kezdoErtek: int = int(input())

print("Vég Érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek +1, 1):
    if(i % 5 == 0 and i % 7 == 0):
        ottelOszthato += 1
        hettelOszthato += 1
    elif(i % 5 == 0):
        ottelOszthato += 1
    elif(i % 7 == 0):
        hettelOszthato += 1

if(hettelOszthato < ottelOszthato):
    print("Az öttel osztható számok összege a nagyobb")
elif(ottelOszthato < hettelOszthato):
    print("A héttel osztható számok összege a nagyobb")
elif(ottelOszthato == hettelOszthato):
    print("Egyenlőek")