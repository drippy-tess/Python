class Gpu:
    def __init__(self, gyarto: str, tipus: str, ram: int) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.ram = ram

     def __str__(self) -> str:
        return f"A Videókártya márkája és típusa: {self.gyarto} {self.tipus}, Memória mérete: {self.ram}GB"