from Motorkerekpar import Motorkerekpar
from Tulajdonos import Tulajdonos

tulaj: Tulajdonos = Tulajdonos("Kovács János", "1990. október 20.", "Férfi", "Debrecen")
motorKerekpar: Motorkerekpar = Motorkerekpar("Honda", "CB600F", "Hornet", 70, 176, 599, tulaj)
print(motorKerekpar)