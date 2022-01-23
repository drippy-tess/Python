import os
import time
import random

szam1: int = None
szam2: int = None
rnd: int = 0
atlag: int = 0
neggyelOszthato: int = 0
nagyobb: int = 0
temp: str = ""

while(szam1 == None or (szam1 % 2 == 1)):
    temp = input("Kérem adja meg az első számot: ")
    if(temp.isdigit()):
        szam1 = int(temp)
        temp = ""
    else:
        print("Nem számot adott meg!")
        time.sleep(2)
        os.system("cls")

while(szam2 == None or szam2 < szam1 or (szam2 % 2 == 0)):
    temp = input("Kérem a második számot: ")
    if(temp.isdigit()):
        szam2 = int(temp)
    else:
        print("Nem számot adott meg!")
        time.sleep(2)
        os.system("cls")

rnd = random.randint(szam1, szam2)
atlag = (szam1 + szam2) /2
nagyobb = abs(szam2) - abs(szam1)

if(abs(nagyobb) > abs(rnd)):
    print(f"A {szam2} számhoz van közelebb az {rnd}.")
elif(nagyobb == rnd):
    print("A két szám egyenlő távolságban van.")
else:
    print(f"A {szam1} számhoz van közelebb az {rnd}.")

for i in range(szam1, szam2 + 1, 1):
    if(i % 4 == 0):
        neggyelOszthato += 1

print(f"A két szám átlaga: {atlag}.")
print(f"A néggyel osztható számok száma: {neggyelOszthato}.")