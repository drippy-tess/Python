#"""
#4 – Írj egy mértékegység konvertáló programot. Az átalakítást Celsius-ból függvénnyel oldjuk meg amely két paramétert kap!
#   Az első egy hőmérséklet érték, a második paraméter pedig azt jelzi milyen mértékegységre akarjuk átkonvertálni (’F’: Fahrenheit, ’K’: Kelvin). 
#   (K = C+273,15; F = 9/5*C+32).
#   Egyes logikai egészeket alkotó műveleteket függvényekkel oldjuk meg.
#"""

import time
import os
import datetime

celsius: float = None
atvaltasMertekegysege: str = None
atvaltottMennyiseg: float = None

#hiba kiirása
def hiba(szoveg: str) -> None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

#hőm. bekerese c-ben
def homersekletBekeres() -> float:
    eredmeny: float = None

    while(eredmeny == None):
        data: str = input("adja meg a hőmérsékletet celsiusban: ")
        if(data.replace(".", "").replace("-", "").isdigit()):
            eredmeny = float(data)
            return eredmeny
        else:
            hiba("Nem jó a bemeneti adat")


#F vagy K-ba váltunk
def valtasValasztas () -> str:
    eredmeny: str = None

    while(eredmeny == None):
        data: str = input("Kérém a váltás módját: [F] vagy [K] \n")
        if(data.capitalize() == "K" or data.capitalize() == "F"):
            eredmeny = data
            return eredmeny
        else:
            hiba("ilyen opció nincs")

#átváltás
def atvaltas (fokCelsius: float, mire: str) -> float:
    if(mire == "K"):
        return fokCelsius + 273,15
    elif (mire == "F"):
        return 9/5 * fokCelsius + 32

#kiírás
def kiiras (fokCelsius: float, atvaltottFok: float, mertekegyseg: str) -> float:
    print(f"{fokCelsius}C = {atvaltottFok}{mertekegyseg}")

celsius= homersekletBekeres()
valtasValasztas= valtasValasztas()
atvaltottMennyiseg= atvaltas(celsius, atvaltasMertekegysege)
kiiras(celsius, atvaltottMennyiseg, atvaltasMertekegysege)