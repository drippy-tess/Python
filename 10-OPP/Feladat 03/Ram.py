class Ram:
    def __init__(self, gyarto: str, tipus: str, meret: int, sebesseg: int):
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.meret = meret
        self.sebesseg = sebesseg

     def __str__(self) -> str:
        return f"A memória gyártója és típusa: {self.gyarto} {self,tipus}, Mérete: {self.meret}, Sebessége: {self.sebesseg}"