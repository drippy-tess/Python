import os
import time

def tizedesSzamBeolvasasa(szoveg: str) -> float:
 szam: float = None
 while(szam == None):
     data: str = input(szoveg)
     if(data.replace("-", "").replace(".","").isdigit()):
         szam = float(data)
         return szam
     else:
        print("Nem számot adoot meg!")
        time.sleep(2)
        os.system("cls")

def tizedesSzamBeolvasasa(szoveg: str) -> int:
 szam: int = None
 while(szam == None):
     data: str = input(szoveg)
     if(data.replace("-", " ").isdigit()):
         szam = int(data)
         return szam
     else:
        print("Nem számot adoot meg!")
        time.sleep(2)
        os.system("cls")

def nevBekeres() -> str:
    nev: str = None

    while(nev == None):
        data: str = input("Kérem a nevét: ")

        #A len függvény megviszgálja, hogy hány karaterből áll a beviteli érték
        if(len(data) < 3):
            print("Túl rövid a név, minimum 3 karakter!")
            time.sleep(2)
            os.system("cls")
        else:
            nev = data

    return nev