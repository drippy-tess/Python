import math

class Egyenlooldalu:
    
    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__()

        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return f"A oldal = {self.a}\nB oldal = {self.b}\nC oldal = {self.c}\nEgyenlő oldalú háromszög területe = {self.egyenloOldaluHaromszogTerulet()}\nEgyenlő oldalú háromszög kerülete = {self.egyenloOldaluHaromszogKerulet()}"

    def egyenloOldaluHaromszogTerulet(self) -> float:
        m: float = (math.sqrt(3) / 2) * self.a
        return (self.a * m) / 2

    def egyenloOldaluHaromszogKerulet(self) -> float:
        return self.a * 3