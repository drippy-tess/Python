from typing import *
from Levelezesicim import Levelezesicim
from Jatekosok import Jatekosok

class Csapat:
    def __init__(self, nev: str, jatekosok: List[Jatekosok], levelezesicim: Levelezesicim) -> None:
        super().__init__()

        self.nev: str = nev
        self.jatekosok: List[Jatekosok] = jatekosok
        self.levelezesicim: Levelezesicim = levelezesicim

    def __str__(self) -> str:
        output: str = f"A csapat neve: {self.nev}\n{self.levelezesicim}"
        for jatekos in self.jatekosok:
            output += f"\n{jatekos}"
        
        return output

    def legjobbJatekos(self) -> Jatekosok:
        max: Jatekosok = self.jatekosok[0]

        for i in range(1, len(self.jatekosok)):
            if(max.pontszam < self.jatekosok[i].pontszam):
                max = self.jatekosok[i]

        return max

    def legtobbMez(self) -> List[Jatekosok]:
        temp: self.jatekosok.copy()

        for i in range(0, len(self.jatekosok)):
            for j in range(i, len(self.jatekosok)):
                if(self.jatekosok[j].mezSzam < self.jatekosok[i].mezSzam):
                    temp: self.jatekosok[i]
                    self.jatekosok[i] = self.jatekosok[j]
                    self.jatekosok[j] = temp
        
        return self
