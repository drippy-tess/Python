from roplabda import Roplabda
from typing import *
from roplabdaio import RoplabdaIO
from feladatok import Feladatok

roplabdazok: List[Roplabda] = RoplabdaIO.read("adatok.txt")
print("A röplabdázók adatai: \n")
for roplabdas in roplabdazok:
    print(f"{roplabdas}\n")

Feladatok.utoJatekos(roplabdazok)
print("Az ütő játékosok exportja megtörtént!")

Feladatok.csapattagok(roplabdazok)
print("A csapat szerinti szétválogatás megtörtént!")

Feladatok.magassagok(roplabdazok)
print("A csapatok embereinek magasságának exportja növekvő sorrendben megtörtént!")