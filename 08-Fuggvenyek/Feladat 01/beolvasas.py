import os
import time

def tizedesSzamBeolvasasa(szoveg: str) -> float:
 szam: float = None
 while(szam == None):
     data: str = input(szoveg)
     if(data.replace("-", " ").isdigit()):
         szam = float(data)
         return szam
     else:
        print("Nem számot adoot meg!")
        time.sleep(2)
        os.system("cls")