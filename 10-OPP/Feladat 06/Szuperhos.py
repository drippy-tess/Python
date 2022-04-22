import random

class Szuperhos:
    def init(self, nev: str) -> None:
        super().__init__()

        self.nev: str = nev
        self.ero: int = random.randint(50,100)
        self.eletpont: int = random.randint(60,90)

    def __str__(self) -> str:
        return f"A szuperhős neve: {self.nev}, ereje: {self.ero}, életpont: {self.eletpont}"

    def Tamad(self, ellenseg: "Szuperhos") -> bool:
        nyert: bool = None

        if(self.ero > ellenseg.eletpont):
            nyert = True
            return nyert
        elif(self.ero < ellenseg.eletpont):
            nyert = False
            return nyert
        else:
            nyert = None
            return nyert