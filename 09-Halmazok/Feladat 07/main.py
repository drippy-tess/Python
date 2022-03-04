from typing import *
import random
import time
import os

kisHalmaz: List[int] = []
nagyHalmaz: List[int] = []
atlag: float = None
osszefuzottHalmaz: List[int] = []
sorbarendezettHalmaz: List[int] = []
elemSzam: int = None

def szamBeolvasasa(kezdoErtek: int, vegErtek: int) -> int:
    eredmeny: int = None
    temp: str = ""

    while(eredmeny == None):
        temp = input("Kérem adja meg a számot:")
        if(temp.isdigit()):
            if(int(temp) >= kezdoErtek and int(temp) <= vegErtek):
                eredmeny = int(temp)
                return eredmeny
            else:
                print("Nem a kezdő és a vég érték között adott meg számot!")
                time.sleep(2)
                os.system("cls")
        else:
            print("Nem számot adott meg!")
            time.sleep(2)
            os.system("cls")

def halmazFeltoltese(elemekSzama: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(0, elemekSzama, 1):
        eredmeny.append(random.randint(1, 10))
    
    return eredmeny

def listaOsszefuzes(halmaz1: List[int], halmaz2: List[int]) -> List[int]:
    eredmeny: List[int] = halmaz1.copy()
    for item in halmaz2:
        eredmeny.append(item)

    return eredmeny

def NovekvoSorrendbeRakas(halmaz: List[int]) -> None:
    temp: int = None
    
    for i in range(0, len(halmaz)-1, 1):
        for j in range(i + 1, len(halmaz), 1):
            if(halmaz[j] < halmaz[i]):
                temp = halmaz[i]
                halmaz[i] = halmaz[j]
                halmaz[j] = temp

def osszeadas(halmaz: List[int]) -> int:
    eredmeny: int = 0
    for item in halmaz:
        eredmeny += item

    return eredmeny 

elemSzam = szamBeolvasasa(1, 5)
kisHalmaz = halmazFeltoltese(elemSzam)
print(kisHalmaz)

elemSzam = szamBeolvasasa(5, 10)
nagyHalmaz =  halmazFeltoltese(elemSzam)
print(nagyHalmaz)

osszefuzottHalmaz = listaOsszefuzes(kisHalmaz, nagyHalmaz)
print(osszefuzottHalmaz)

NovekvoSorrendbeRakas(osszefuzottHalmaz)
print(f"Növekvő sorrendbe rakott halmaz: {osszefuzottHalmaz}")

atlag = osszeadas(osszefuzottHalmaz) / len(osszefuzottHalmaz)
print(f"A halmaz elemeinek átlaga: {atlag}")