from typing import List
from typing import *
from Levelezesicim import Levelezesicim
from Jatekosok import Jatekosok
from Csapat import Csapat

levelezesiCim: Levelezesicim = Levelezesicim("Szeged", 6724, "Csongrád megye", "Vértói út", 7)

jatekos1: Jatekosok = Jatekosok("Borsi","Levente", 1, "Libero")
jatekos2: Jatekosok = Jatekosok("Piti","Richárd", 3, "Center")
jatekos3: Jatekosok = Jatekosok("Péter","Márk", 7, "Feladóátló")
jatekos4: Jatekosok = Jatekosok("Polyák", "Ábel", 8, "4-es ütő")
jatekos5: Jatekosok = Jatekosok("Tomás", "Dileó", 9, "Feladó")
jatekosok: List[Jatekosok] = [jatekos1, jatekos2, jatekos3, jatekos4, jatekos5]

csapat: Csapat = Csapat("SZRSE", jatekosok, levelezesiCim)

print(csapat)