from Pc import Pc
from Processzor import Processzor
from Gpu import Gpu
from Ram import Ram
from Psu import Psu
from Ssd import Ssd
from Mobo import Mobo

ssd: Ssd = Ssd("WD", "Green", 240)
psu: Psu = Psu("EVGA", 500, "80+ Bronze")
ram: Ram = Ram("ZADAK", "Spark RGB", 16, 3200)
mobo: Mobo = Mobo("GIGABYTE", "X570 Gaming X", "AMD X570")
gpu: Gpu = Gpu("NVIDIA", "GeForece GTX 1660 Super Gaming OC", 6)
proci: Processzor = Processzor("AMD", "Ryzen 5 2600X", 2600, 16)
pc: Pc = Pc(proci, gpu, mobo, ram, psu, ssd)
print(pc)