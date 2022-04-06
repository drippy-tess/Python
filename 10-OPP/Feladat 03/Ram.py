class Ram:
    def __init__(self, gyarto: str, tipus: str, meret: int, sebesseg: int) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.meret = meret
        self.sebesseg = sebesseg
        

    def __str__(self) -> str:
        return f"A memória márkája, és típusa: {self.gyarto} {self.tipus}\nMérete:{self.meret}GB\nSebessége: {self.sebesseg}MHZ"