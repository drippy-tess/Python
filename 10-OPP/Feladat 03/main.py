from Processzor import Processzor
from Gpu import Gpu
from Mobo import Mobo
from Ram import Ram
from Psu import Psu
from Ssd import Ssd

ssd: Ssd = Ssd("WD", "Green", "240GB")
psu: Psu = Psu("EVGA", 500, "80+ Bronze")
ram: Ram = Ram("ZADAK", "Spark", 16, 3200)
mobo: Mobo = Mobo("GIGABYTE", "X570 Gaming X", "AMD X570")
gpu: Gpu = Gpu("NVIDIA", "GeForce GTX 1660 Super", 6)
proci: Processzor = Processzor("AMD", "Ryzen 5 2600X", 2600, 16, gpu, mobo, ram, psu, ssd)
print(proci)