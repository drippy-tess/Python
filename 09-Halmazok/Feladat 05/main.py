#Könyvtárak importálása
from typing import *
import random
import time
import os

#Változók
honapok: Tuple[str] = (
    "Január",
    "Február",
    "Március",
    "Április",
    "Május",
    "Június",
    "Július",
    "Augusztus",
    "Szeptember",
    "Október",
    "November",
    "December"
)
fizetesek: List[int] = []
szjaErteke: float = None
tbErteke: float = None
nyugdijAlap: float = None

#Függvények
def fizetsekGeneralasa() -> List[int]:
    eredmeny: List[int] = []
    
    for i in range(0, 12, 1):
        eredmeny.append(random.randint(200, 1000))
        
    return eredmeny

def fizetesekKiirasa(berek: List[int], honapok: Tuple[str]) -> None:
    for index in range(0, 12, 1):
        print(f"{honapok[index]} - {berek[index]}e HUF")

def fizetesekOsszege(berek: List[int]) -> int:
    osszeg: int = 0
    
    for ber in berek:
        osszeg += ber
        
    return osszeg

def SZJA(berek: List[int]) -> float:
    osszeg: int = fizetesekOsszege(berek)
    return osszeg * 0.335

def TB(szja: float) -> float:
    return szja * 0.45

#Főprogram
fizetesek = fizetsekGeneralasa()
fizetesekKiirasa(fizetesek, honapok)

szjaErteke = SZJA(fizetesek)
tbErteke = TB(szjaErteke)

print(f"SZJA: {szjaErteke}e HUF")
print(f"TB: {tbErteke}e HUF")