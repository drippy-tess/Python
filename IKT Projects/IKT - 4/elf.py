from champion import Champion
import random

class Elf(Champion):
    def __init__(self, name: str, race: str) -> None:
        Champion.__init__(self, name, race)

    def __str__(self) -> str:
        return f"{self.name}, {self.race}, {self.hp}, {self.manna}, {self.power}, {self.armor}"

    def castASpell(self) -> None:
        random: int = random.randint(10, 50)
        
        self.power += random
        self.hp += 100
        self.manna -= 50
        self.armor += 1