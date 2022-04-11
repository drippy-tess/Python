from typing import *
from Tanulo import Tanulo

class Osztaly:
    def __init__(self,osztalyNeve: str, tanulo: List[Tanulo], tanulo1: List[Tanulo], tanulo2: List[Tanulo]) -> None:
        super().__init__()

        self.osztalyNeve: str = osztalyNeve
        self.tanulo: List[Tanulo] = tanulo
        self.tanulo1: List[Tanulo] = tanulo1
        self.tanulo2: List[Tanulo] = tanulo2

        halmaz: List[Tanulo] = []
        halmaz.append(tanulo)
        halmaz.append(tanulo1)
        halmaz.append(tanulo2)
    
    def __str__(self) -> str:
        return f"Az osztály neve: {self.osztalyNeve}\n{self.tanulo}\n{self.tanulo1}\n{self.tanulo2}"