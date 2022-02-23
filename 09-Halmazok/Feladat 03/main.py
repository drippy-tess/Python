from typing import *
import random

dobasok: List[int] = []
dobasokOsszege: int = None
dobasokAtlaga: float = None
hatosDobasokSzama: int = None
paratlanDobasokSzama: int = None

def dobas(dobasokSzama: int = 7) -> List[int]:
    eredmeny: List[int] = []
    szam: int = None

    for i in range(0, 7, 1):
        szam = random.randint(1, 6)
        eredmeny.append(szam)

    return eredmeny

def dobasOsszeg(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for dobasok in bejarandoHalmaz:
        eredmeny += dobasok

    return eredmeny

def hatosDobasSzam(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0
    
    for dobasok in bejarandoHalmaz:
        if(dobasok == 6):
            eredmeny += 1
    
    return eredmeny

def paratlanDobasSzam(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for dobasok in bejarandoHalmaz:
        if(dobasok % 2 != 0):
            eredmeny += 1
    
    return eredmeny

dobasok = dobas()
print(f"A dobások: {dobasok}")

dobasokOsszege = dobasOsszeg(dobasok)
print(f"A dobások összege: {dobasokOsszege}")

dobasokAtlaga = dobasokOsszege / 7
print(f"A dobások átlaga: {dobasokAtlaga}")

hatosDobasokSzama = hatosDobasSzam(dobasok)
print(f"A hatos dobások száma: {hatosDobasokSzama}")

paratlanDobasokSzama = paratlanDobasSzam(dobasok)
print(f"A páratlan dobások száma: {paratlanDobasokSzama}")