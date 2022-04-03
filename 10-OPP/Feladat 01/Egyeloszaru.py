import math

class Haromszog:
    
    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__()

        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return f"A oldal = {self.a}\nB oldal = {self.b}\nC oldal = {self.c}\nEgyenlő szárú háromszög területe = {self.egyenloSzaruHaromszogTerulet()}\nEgyenlő szárú háromszög területe = {self.egyenloSzaruHaromszogKerulet()}"

    def egyelnoSzaruHaromszogTerulet(self) -> float:
        m: float = math.sqrt((self.b * self.b) - ((self.a * self.a) / 4))
        return (self. a * m) / 2
    
    def egyelnoSzaruHaromszogKerulet(self) -> float:
        return self.a + (2 * self.b)