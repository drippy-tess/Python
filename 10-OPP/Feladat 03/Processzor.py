from Gpu import Gpu
from Ram import Ram
from Psu import Psu
from Ssd import Ssd
from Mobo import Mobo

class Processzor:
    def __init__(self, gyarto: str, tipus: str, orajel: int, cache: int, gpu: Gpu, mobo: Mobo, ram: Ram, psu: Psu, ssd: Ssd) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.orajel = orajel
        self.cache = cache
        self.gpu = gpu
        self.mobo = mobo
        self.ram = ram
        self.psu = psu
        self.ssd = ssd

    def __str__(self) -> str:
        return f"A processzor márkája és típusa: {self.gyarto} {self.tipus}\nÓrajele: {self.orajel}MHZ\nCache mérete: {self.cache}MB\n{self.gpu}\n{self.mobo}\n{self.ram}\n{self.gpu}\n{self.psu}\n{self.ssd}"