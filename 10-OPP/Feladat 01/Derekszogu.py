class Derekszogu:
    
    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__()

        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return f"A oldal = {self.a}\nB oldal = {self.b}\nC oldal = {self.c}\nDerekszögű háromszög területe = {self.derekSzoguHaromszogTerulet()}\nDerekszögű háromszög kerülete = {self.derekSzoguHaromszogKerulet()}"
    
    def derekSzoguHaromszogTerulet(self) -> float:
        return (self.a * self.b) / 2

    def derekSzoguHaromszogKerulet(self) -> float:
        return self.a + self.b + self.c