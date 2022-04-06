class Ssd:
    def __init__(self, gyarto: str, tipus: str, meret: int) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.meret = meret
        

    def __str__(self) -> str:
        return f"Az SSD márkája, és típusa: {self.gyarto} {self.tipus}\nMérete: {self.meret}GB"