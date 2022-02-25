from typing import *
import random

dobasok: List[int] = []
dobasokOsszege: int = None
dobasokAtlaga: float = None
hatosDobasokSzama: int = None
paratlanDobasokSzama: int = None
legtobbetEloforduloSzamok: List[int] = []

def dobas(dobasokSzama: int = 7) -> List[int]:
    eredmeny: List[int] = []
    szam: int = None

    for i in range(0, 7, 1):
        szam = random.randint(1, 6)
        eredmeny.append(szam)

    return eredmeny

def dobasOsszeg(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for dobas in bejarandoHalmaz:
        eredmeny += dobas

    return eredmeny

def hatosDobasSzam(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0
    
    for dobas in bejarandoHalmaz:
        if(dobas == 6):
            eredmeny += 1
    
    return eredmeny

def paratlanDobasSzam(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for dobas in bejarandoHalmaz:
        if(dobas % 2 != 0):
            eredmeny += 1
    
    return eredmeny

def legnagyobbKulcsErtek(szotar: Dict[int, int]) -> List[int]:
    kulcs: int = None
    ertek: int = 0
    eredmeny: List[int] = []

    #a legnagyobb érték kikeresése a szótárból
    for key, value in szotar.items(): #végiglépkedünk a szótár össze elemén kulcs-érték párokkal
        if(szotar[key] > ertek):
            kulcs = key
            ertek = szotar[key]

    for key, value in szotar.items(): #kikeressük azokat a kulcsokat melyeknek az értéke egyenlő az érték változóval, mivel azok a kulcsok(dobások) száma fordul elő legtöbbször
        if(szotar[key] == ertek):
            eredmeny.append(key)
    
    return eredmeny

def legtobbetEloforduloSzam(bejarandoHalmaz: List[int]) -> List[int]:
    szotar: Dict[int, int] = {} #Dict[kulcs -> szám, érték -> szám előfordulási száma]
    eredmeny: List[int] = []
   #meghatározzuk az előfordulási számokat
    for szam in bejarandoHalmaz:
        if(szam in szotar):
           szotar[szam] += 1 #szotar [szam] -> a kulcshoz tartozó értéket adja vissza
        else:
            szotar[szam] = 1

    eredmeny = legnagyobbKulcsErtek(szotar)
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

legtobbetEloforduloSzamok = legtobbetEloforduloSzam(dobasok)
print(f"A legtöbbet előforduló szám(ok): {legtobbetEloforduloSzamok}")