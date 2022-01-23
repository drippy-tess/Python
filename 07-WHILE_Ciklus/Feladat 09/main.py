import os
import time

szam: int = None
temp: str = ""

while(szam == None or szam > 999 or szam < 100 ):
    temp = input("Kérem adjon meg egy 3 jegyű számot!")
    if(temp.isdigit()):
        szam = int(temp)
    else:
        print("Nem számot adott meg!")

if(szam % 7 == 0 ):
    print(f"A beírt szám 3 jegyű és osztható 7-tel ({szam}).")
else:
    print("Rossz szám!")