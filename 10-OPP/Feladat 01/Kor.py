import math

class Kor:
    #konstruktor
    def __init__(self, sugar: float) -> None:
        super().__init__()

        self.sugar = sugar

    def __str__(self) -> str:
        return f"Sugár = {self.sugar}\nKerület = {self.kerulet()}\nTerület = {self.terulet()}"

    def kerulet(self) -> float:
        return 2*self.sugar*math.pi

    def terulet(self) -> float:
        return self.sugar*self.sugar*math.pi