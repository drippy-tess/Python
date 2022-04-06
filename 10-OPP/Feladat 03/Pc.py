from Processzor import Processzor
from Gpu import Gpu
from Ram import Ram
from Psu import Psu
from Ssd import Ssd
from Mobo import Mobo

class Pc:
    def __init__(self, cpu: Processzor, gpu: Gpu, mobo: Mobo, ram: Ram, psu: Psu, ssd: Ssd) -> None:
        super().__init__()

        self.cpu = cpu
        self.gpu = gpu
        self.mobo = mobo
        self.ram = ram
        self.psu = psu
        self.ssd = ssd

    def __str__(self) -> str:
        return f"{self.cpu}\n{self.gpu}\n{self.mobo}\n{self.ram}\n{self.gpu}\n{self.psu}\n{self.ssd}"