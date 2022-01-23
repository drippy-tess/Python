import os
import time

szam: int = int(input("Írjon be egy számot: "))
szam1: int = 0
osszeg: int = 0

osszeg = szam

while (osszeg < 100):
        szam1: int = int(input("Írjon be egy másik számot: "))
        osszeg = osszeg + szam1
        print(f"{osszeg}")

print(f"{osszeg}")