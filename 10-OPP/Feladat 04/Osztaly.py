from typing import *
from Tanulo import Tanulo

class Osztaly:
    def __init__(self,osztalyNeve: str, tanulok: List[Tanulo]) -> None:
        super().__init__()

        self.osztalyNeve: str = osztalyNeve
        self.tanulok: List[Tanulo] = tanulok
    
    def __str__(self) -> str:
        output: str = f"{self.osztalyNeve}\n"
        for tanulo in self.tanulok:
            output += f"\n{tanulo}"
        return output