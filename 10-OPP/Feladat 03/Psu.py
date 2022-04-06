class Psu:
    def __init__(self, gyarto: str, tipus: str, minosites: str) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.minosites = minosites

    def __str__(self) -> str:
        return f"A tápegység márkája, és típusa: {self.gyarto} {self.tipus}\nMinősítése: {self.minosites}"