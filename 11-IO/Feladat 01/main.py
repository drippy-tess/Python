from operator import truediv
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

#5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
Osztaly.atlagfelettiek(diakok, atlag)
print(f"Az osztály átlag feletti diákjainak exportja megtörtént.")

#6 - Van e kitünő tanulónk?
vanE: bool = Osztaly.vanEkitunotanulo(diakok)
if(vanE):
    print(f"Van kitűnő tanuló!")
else:
    print(f"Az osztályban nincs kitűnő tanuló!")

#7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
diakAtlagok: Dict[str, int] = Osztaly.kitunoTanulo(diakok)
print(f"Az osztáyban átlag szerint a következő eredményt érték el a diákok:")
for (key, value) in diakAtlagok.items():
    print(f"\t- {key} : {value}")