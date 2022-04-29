from typing import *
import random

class Jatekos:
    def __init__(self, nev: str, tippek: Set[int]) -> None:
        super().__init__
        
        self.nev: str = nev
        self.tippek: Set[int] = set(tippek)

    def __str__(self) -> str:
        return f"A játékos neve: {self.nev}\n Tippjei: {self.tippek}"

    def talalt(self, joszamok: Set[int]) -> Set[int]:
        return self.tippek.intersection(joszamok)