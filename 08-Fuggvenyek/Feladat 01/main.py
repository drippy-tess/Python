from matematikafuggvenyek import *
from inputLib import *

osszeg: float = 0
kulonbseg: float = 0
szorzat: float = 0
hanyados: float = 0
elsoSzam: float = 0
masodikSzam: float = 0

elsoSzam = tizedesSzamBeolvasasa("Kérem adja meg az első számot! ")
masodikSzam = tizedesSzamBeolvasasa("Kérem adja meg a második számot! ")

osszeg = osszeadas(elsoSzam, masodikSzam)
kulonbseg = kivonas(elsoSzam, masodikSzam)
szorzat = szorzas(elsoSzam, masodikSzam)
hanyados = osztas(elsoSzam, masodikSzam)

print(f"A számok összege {osszeg}, különbsége {kulonbseg}, szorzata {szorzat} és hányadosa {hanyados}.")