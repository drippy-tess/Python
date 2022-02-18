"""Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal:
"""

#Könyvtárak importálása
from typing import *
import random
import time
import os

#Változók
halmaz: List[int] = []
elemekSzama: int = None
osszeg: int = None
ketjegyuSzamok: int = None
paratlanSzamOsszeg: int = None
nullraVegzodoSzamok: int = None
rendezettHalmaz: List[int]
maximum: int = None
minimumIndex: int = None

#Függvények
def hiba(uzenet:str) -> None:
    print(uzenet)
    time.sleep(2)
    os.system("cls")

def halmazKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

def elemszamBekerese() -> int:
    eredmeny: int = None
    temp: str = None

    while(eredmeny == None):
        temp: str = input("Kérem adja meg a halmaz elemeinek számát: ")
        if(temp.isdigit()):
            eredmeny = int(temp)
            if(eredmeny < 2):
                hiba("A halmaz elemeinek száma legalább kettőnek kell lennie!")
        else:
            hiba("Nem számot adott meg!")    
    return eredmeny

def listaFeltolteseRandomSzamokkal(elemszam: int) -> List[int]:
    eredmeny: List[int] = []
    for i in range (elemszam):
        eredmeny.append(random.randint(-10, 10))
        time.sleep(0.005)
    return eredmeny

def halmazKiirasaFordítottSorrendben(kiirandoHalmaz:List [int]) -> None:
    max: int = len(kiirandoHalmaz) - 1
    for index in range(max, -1, -1):
        print(f"{kiirandoHalmaz[index]}", end="\t")

def szum(osszeadandoHalmaz: List[int]) -> int:
    osszeg: int = 0

    for item in osszeadandoHalmaz:
        osszeg += item

    return osszeg

def parosSzamokKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        if(item % 2 == 0):
            print(f"{item}", end="\t")

def ketjegyuSzamokSzama(keresesHalmaza:List[int]) -> int:
    eredmeny: int = 0
    for item in keresesHalmaza:
        if(abs(item) > 9 and abs(item) < 100):
            eredmeny += 1
    return eredmeny

def egyjegyuSzamokKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        if(abs(item) < 10):
            print(f"{item}", end="\t")

def paratlanSzamokOsszege(keresesHalmaz: List[int]) -> int:
    eredmeny: int = 0
    for item in keresesHalmaz:
        if(item % 2 == 1):
            eredmeny += item
    return eredmeny

def nullaraVegzodoSzamokSzama(keresesHalmaz: List[int]) -> int:
    eredmeny: int = 0
    for item in keresesHalmaz:
        if(item % 10 == 0):
            eredmeny += 1

    return eredmeny

def novekvoSorrend(keresesHalmaz: List[int]) -> List[int]:
    temp: int = None
    for i in range(0, len(keresesHalmaz) -1, 1):
        for j in range(i + 1, len(keresesHalmaz), 1):
            if(keresesHalmaz[j] < keresesHalmaz[i]):
                temp = keresesHalmaz[i]
                keresesHalmaz[i] = keresesHalmaz[j]
                keresesHalmaz[j] = temp
    
    return keresesHalmaz

def legnagyobbErtek(keresesHalmaz: List[int]) -> int:
    max: int = keresesHalmaz[0]
    for index in range (1, len(keresesHalmaz), 1):
        if(keresesHalmaz[index] > max):
            max = keresesHalmaz[index]
    return max

def legkissebbErtekIndexe(keresesHalmaz: List[int]) -> int:
    index: int = 0
    min: int = keresesHalmaz[index]
    for i in range (1, len(keresesHalmaz), 1):
        if(keresesHalmaz[i] < min):
            min = keresesHalmaz[i]
            index = i
    
    return index

#Főprogram
elemekSzama = elemszamBekerese()
halmaz = listaFeltolteseRandomSzamokkal(elemekSzama)

os.system("cls")
print("A halmaz elemei: ")
halmazKiirasa(halmaz)

print("\n")
print("Halmaz elemei fordított sorrendben: ")
halmazKiirasaFordítottSorrendben(halmaz)

osszeg = szum(halmaz)
print("\n")
print(f"Az elemek összege:{osszeg}")

print("\n")
print(f"A halmaz átlaga:{osszeg / elemekSzama}")

print("\n")
print("A halmaz páros elemei: ")
parosSzamokKiirasa(halmaz)

ketjegyuSzamok = ketjegyuSzamokSzama(halmaz)
print("\n")
print(f"A halmazban {ketjegyuSzamok} kétjegyű szám van.")

print("\n")
print(f"A halmaz egyjegyű elemei: ")
egyjegyuSzamokKiirasa(halmaz)

paratlanSzamOsszeg = paratlanSzamokOsszege(halmaz)
print("\n")
print(f"A halmaz páratlan számok elemeinek összege: {paratlanSzamOsszeg}")

nullraVegzodoSzamok = nullaraVegzodoSzamokSzama(halmaz)
print("\n")
print(f"A halmaz nullára végződő elemeinek összege: {nullraVegzodoSzamok}")

"""
rendezettHalmaz = novekvoSorrend(halmaz)
print("\n")
print(f"Növekvő sorrendbe rendezett halmaz: {rendezettHalmaz}")

"""

maximum = legnagyobbErtek(halmaz)
print("\n")
print(f"A halmaz legnagyobb eleme: {maximum}")

minimumIndex = legkissebbErtekIndexe(halmaz)
print("\n")
print(f"A legkissebb érték indexe: {minimumIndex}")