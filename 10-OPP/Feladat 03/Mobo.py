class Mobo:
    def __init__(self, gyarto: str, tipus: str, chipset: str) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.chipset = chipset
        

    def __str__(self) -> str:
        return f"Az alaplap márkája, és típusa: {self.gyarto} {self.tipus}\nChipset: {self.chipset}"