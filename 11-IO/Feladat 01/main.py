from diak import Diak
from typing import *
from diakio import DiakIO
from osztaly import Osztaly

diakok: List[Diak] = DiakIO.read("adatok.txt")
#1 - Írjuk ki minden diák adatát a képernyőre!
print("A diakok adatai: \n")
for diak in diakok:
    print(f"{diak}\n")

#2 - Hány diák jár az osztályba?
print(f"Az osztályba járó diákok száma {len(diakok)}.\n")

#3 - Mennyi az osztály átlaga?
atlag: float = Osztaly.atlag(diakok)
print(f"Az osztály átlaga: {atlag:1.2f}")#két tizedes jegyre kerekítve

#4 - Keressük a legnagyobb átlagot elért érettségizőt és írjuk ki az adatait a képernyőre.
print("Az osztály legjobb diákjai: \n")
joDiakok: List[Diak] = Osztaly.legjobbak(diakok)
for diak in joDiakok:
    print(f"{diak}\n")