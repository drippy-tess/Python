from typing import List
from typing import *
from Levelezesicim import Levelezesicim
from Jatekosok import Jatekosok
from Csapat import Csapat

levelezesiCim: Levelezesicim = Levelezesicim("Szeged", 6724, "Csongrád-Csanád megye", "Vértói út", 7)

jatekos1: Jatekosok = Jatekosok("Borsi","Levente", 1, "Libero", 52)
jatekos2: Jatekosok = Jatekosok("Piti","Richárd", 3, "Center", 12)
jatekos3: Jatekosok = Jatekosok("Péter","Márk", 7, "Feladóátló", 87)
jatekos4: Jatekosok = Jatekosok("Polyák", "Ábel", 8, "4-es ütő",54)
jatekos5: Jatekosok = Jatekosok("Tomás", "Dileó", 9, "Feladó", 23)
jatekosok: List[Jatekosok] = [jatekos1, jatekos2, jatekos3, jatekos4, jatekos5]

csapat: Csapat = Csapat("SZRSE", jatekosok, levelezesiCim)

print(csapat)

print("A legtöbb pontszámmal rendelkező játékos:")
print(csapat.legjobbJatekos())