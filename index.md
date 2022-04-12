## Welcome 
This project files are written in Python.

## Example code

```
from typing import *
import random
import os

halmaz: List[int] = []
elemSzam: int = random.randint(10, 20)
osszeg: int = None
atlag: float = None
otszazFelettiSzamokSzama: int = None

def halmazFeltoltes(elemekSzama: int) -> List[int]:
    eredmeny: List[int] = []
    szorzo: int = 1
    szam: int = None

    for i in range(0, elemekSzama, 1):
        szam = random.randint(100, 999)
        eredmeny.append(szam * szorzo)
        szorzo *= -1
    
    return eredmeny

def halmazKiirasa(kiirandoHalmaz: List[int]) -> None:
    for szam in kiirandoHalmaz:
        print(f"{szam}", end="\t")

def szum(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0
    
    for szam in bejarandoHalmaz:
        eredmeny += szam
    return eredmeny

def otszazFelettiSzamokSzamanakMeghatarozasa(bejarandoHalmaz:List[int]) -> int:
    eredmeny: int = 0

    for szam in bejarandoHalmaz:
        if(szam > 500):
            eredmeny += 1
    return eredmeny

halmaz = halmazFeltoltes(elemSzam)
os.system("cls")
halmazKiirasa(halmaz)

osszeg = szum(halmaz)
print("\n")
print(f"A halmaz elemeinek összege: {osszeg}")

atlag = osszeg / elemSzam
print("\n")
print(f"A halmaz eleminek átlaga: {atlag}")

otszazFelettiSzamokSzama = otszazFelettiSzamokSzamanakMeghatarozasa(halmaz)
print("\n")
print(f"A halmazban {otszazFelettiSzamokSzama} ötszáz feletti szám van.")
```
