from​ ​Gpu​ ​import​ ​Gpu 
from​ ​Mobo​ ​import​ ​Mobo 
from​ ​Ram​ ​import​ ​Ram 
from​ ​Psu​ ​import​ ​Psu 
from​ ​Ssd​ ​import​ ​Ssd

class ​Processzor: 
​    ​def​ ​__init__​(​self​, ​gyarto: ​str​, ​tipus: ​str​, ​orajel: ​int, ​cache: ​int, gpu: Gpu, mobo: Mobo, ram: Ram, psu: Psu, ssd: Ssd) ​->​ ​None​: 
​        ​super​().​__init__​()
    
        self.gyarto = gyarto
        self.tipus = tipus
        self.orajel = orajel
        self.cache = cache
        self.gpu = gpu
        self.mobo = mobo
        self.ram = ram
        self.psu = psu
        self.sdd = ssd
    
    def​ ​__str__​(​self​) ​->​ ​str​: 
​        ​return​ ​f"A processor típusa és gyártója: ​{​self​.gyarto}​ {self.tipus}\n​Órajel: ​{​self​.​orajel}​\nCache: ​{​self​.​cache}​\n{self.gpu}\n{self.mobo}\n{self.ram}\n{self.psu}\n{self.ssd}"