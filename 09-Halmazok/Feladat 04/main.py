from types import LambdaType
from typing import *
import random

elemekSzama: int = random.randint(10, 20)
halmaz: List[int] = []
pozitivHalmaz: List[int] = []

def halmazFeltoltese(elemSzam: int) -> List[int]:
    eredmeny: List[int] = []

    for item in range(0, elemSzam):
        eredmeny.append(random.randint(-100, 100))
    
    return eredmeny

def kiiras(kiirandoHalmaz: List[int]) -> None:
    for szam in kiirandoHalmaz:
        print(f"{szam}", end = "\t")

def pozitivhalmazFeltoltese(bejarandoHalmaz: List[int]) -> List [int]:
    eredmeny: List[int] = []

    for szam in bejarandoHalmaz:
        if(szam >= 0):
            eredmeny.append(szam)
    
    return eredmeny

halmaz = halmazFeltoltese(elemekSzama)
print("A generált halmaz:")
kiiras(halmaz)
print("\n")

pozitivHalmaz = pozitivhalmazFeltoltese(halmaz)
print("A pozitív számokat tartalmazó halmaz: ")
kiiras(pozitivHalmaz)