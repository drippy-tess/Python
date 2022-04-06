class Processzor:
    def __init__(self, gyarto: str, tipus: str, orajel: int, cache: int) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.orajel = orajel
        self.cache = cache

    def __str__(self) -> str:
        return f"A processzor márkája és típusa: {self.gyarto} {self.tipus}\nÓrajele: {self.orajel}MHZ\nCache mérete: {self.cache}MB"