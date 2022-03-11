from typing import *
import random
import time
import os

elemszam: int = None
eredetihalmaz: List[int] = []
harommaloszthatok: List[int] = []
harommaloszthatokosszeg: int = 0
harommaloszthatokatlag: float= 0
otteloszthatodeharommalnemosztahok: List[int] = []
otteloszthatodeharommalnemosztahokosszeg: int = 0
otteloszthatodeharommalnemosztahokatlag: float = 0

def hibakiiras(szoveg: str):
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def elemszambekeres()->int:
    eredmeny: int = None
    data: str = ""

    while(eredmeny == None or eredmeny < 10):
        data = input("Kérem adja meg a 2 halmaz elemszámát (min. 10):  ")
        if(data.replace("-", "").isnumeric()):
            eredmeny = int(data)
            if(eredmeny < 10):
                hibakiiras("Nem megfelelő számot adott meg.")
        else:
            hibakiiras("Nem számot adott meg.")

    return eredmeny

def listatoltes(elemszama: int) -> List[int]:
    eredmeny: List[int] = []
    rndszam: int = 0

    for i in range(elemszama):
        rndszam = random.randint(-100, 100)
        eredmeny.append(rndszam)

    return eredmeny

def harommaloszthatoklist(lista: List[int]) -> List[int]:
    eredmeny: List[int] = []

    for item in lista:
        if (item % 3 == 0):
            eredmeny.append(item)

    return eredmeny

def otteloszthatodeharommalnemosztahoklist(lista: List[int]) -> List[int]:
    eredmeny: List[int] = []

    for item in lista:
        if (item % 3 != 0 and item % 5 == 0):
            eredmeny.append(item)

    return eredmeny

def kiiras(lista: List[int]):
    for item in lista:
        print(f"{item}", end="  ")

def osszeg(lista: List[int]) -> int:
    eredmeny: int = 0

    for item in lista:
        eredmeny += item

    return eredmeny

def melyikatlaganagyobb(otososszeg: int, otosatlag: float, harmasosszeg: int, harmasatlag: float):
    if(otosatlag > harmasatlag):
        print(f"Az öttel osztható átlaga ({otosatlag}, összege: {otososszeg}) nagyobb mint a hárommal osztható átlaga ({harmasatlag}, összege: {harmasosszeg})")
    elif(otosatlag < harmasatlag):
        print(f"Az hárommal osztható átlaga ({harmasatlag}, összege: {harmasosszeg}) nagyobb mint az öttel osztható átlaga ({otosatlag}, összege: {otososszeg})")
    else:
        print(f"Az hárommal osztható átlaga ({harmasatlag}, összege: {harmasosszeg}) egyenlő az öttel osztható átlaga ({otosatlag}, összege: {otososszeg})")

elemszam = elemszambekeres()
eredetihalmaz = listatoltes(elemszam)

harommaloszthatok = harommaloszthatoklist(eredetihalmaz)
harommaloszthatokosszeg = osszeg(harommaloszthatok)
harommaloszthatokatlag = harommaloszthatokosszeg / len(harommaloszthatok)

otteloszthatodeharommalnemosztahok = otteloszthatodeharommalnemosztahoklist(eredetihalmaz)
otteloszthatodeharommalnemosztahokosszeg = osszeg(otteloszthatodeharommalnemosztahok)
otteloszthatodeharommalnemosztahokatlag = otteloszthatodeharommalnemosztahokosszeg / len(otteloszthatodeharommalnemosztahok)

print("Az eredeti halmaz:")
kiiras(eredetihalmaz)

print("\nA halmaz hárommal osztható elemei:")
kiiras(harommaloszthatok)

print("\nA halmaz öttel osztható de hárommal nem osztható elemei:")
kiiras(otteloszthatodeharommalnemosztahok)

print("\n")
melyikatlaganagyobb(otteloszthatodeharommalnemosztahokosszeg, otteloszthatodeharommalnemosztahokatlag, harommaloszthatokosszeg, harommaloszthatokatlag)