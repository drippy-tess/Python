from konyv import Konyv
from typing import *
from konyvio import KonyvIO

konyvek: List[Konyv] = KonyvIO.read("adatok.txt")
print("A könyvek adatai: \n")
for konyv in konyvek:
    print(f"{konyv}\n")
