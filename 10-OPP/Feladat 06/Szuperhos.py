import random

class Szuperhos:
    def __init__(self, nev: str) -> None:
        super().__init__()

        self.nev: str = nev
        self.ero: int = random.randint(50,100)
        self.eletpont: int = random.randint(60,90)

    def __str__(self) -> str:
        return f"A szuperhős neve: {self.nev}, ereje: {self.ero}, életpont: {self.eletpont}"

    def tamad(self, ellenseg: "Szuperhos") -> bool:
        return self.ero >ellenseg.eletpont