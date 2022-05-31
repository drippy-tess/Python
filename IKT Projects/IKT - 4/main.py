from elf import Elf
from human import Human
from orc import Orc

arwen: Elf = Elf("Anwen", "Elf")
print(arwen)

galadriel: Elf = Elf("Galadriel", "Elf")
print(galadriel)

tauirel: Human = Human("Tauirel", "Elf")
print(tauirel)

eowyn: Human = Human("Eowyn", "Human")
print(eowyn)

lurtz: Orc = Orc("Lurtz", "Orc")
print(lurtz)

successArwen = arwen.attack(lurtz)
successGaladriel = galadriel.attack(lurtz)
successTauriel = tauirel.attack(lurtz)
successEowyn = eowyn.attack(lurtz)
print()

if(successArwen == True):
    print("Anwen win!\n")
else:
    print("Arwen loose!\n")
    
if(successGaladriel == True):
    print("Galadriel win!\n")
else:
    print("Galadriel loose!\n")

if(successTauriel == True):
    print("Tauriel win!\n")
else:
    print("Tauriel loose!\n")

if(successEowyn == True):
    print("Eowyn win!\n")
else:
    print("Eowyn loose!\n")