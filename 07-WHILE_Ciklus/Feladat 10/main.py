import os
import time

szam: int = None
temp: str = ""
ottelOszthato: int = 0
tizeneggyelOszthato: int = 0

while(szam == None or szam < 0 or szam > 100):
    temp = input("Kérem adjon meg egy számot: ")
    if(temp.isdigit()):
        szam = int(temp)
    else:
        print("Rossz bevitel!")
        time.sleep(2)
        os.system("cls")

print(f"\n")
for i in range(0, szam +1, 1):
    if(i % 2 == 0):
        print(f"{i}", end=" ")

print(f"\n")
for j in range(0, szam + 1, 1):
    if(j % 5 == 0):
        ottelOszthato += j

print(f"\n")
for k in range(0, szam + 1, 1):
    if(k % 11 == 0):
        tizeneggyelOszthato += 1

print(f"\n")
for l in range(0, szam + 1, 1):
    if(l % 7 == 3):
        print(f"{l}", end=" ")

print(f"A tizeneggyel osztható számok száma: {tizeneggyelOszthato}.")
print(f"Az öttel osztható számok összege: {ottelOszthato}.")