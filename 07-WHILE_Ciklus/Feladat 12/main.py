import os
import time

megtakaritas: float = None
temp: str = ""
honapokSzama: int = 0

while(megtakaritas == None or megtakaritas > 50000 or megtakaritas < 10000):
    temp = input("Kérem adja meg a megtakarítását: ")
    if(temp.isdigit()):
        megtakaritas = int(temp)
    else:
        print("Nem számot adott meg!")
        time.sleep(2)
        os.system("cls")

while(megtakaritas < 100000):
    megtakaritas = megtakaritas * 1.02
    honapokSzama += 1

print(f"{honapokSzama} hónap alatt érte el a pénzem 100000 Forintot, 2%-os kamattal.")