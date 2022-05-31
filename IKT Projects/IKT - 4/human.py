from champion import Champion
import random

class Human(Champion):
    def __init__(self, name: str, race: str) -> None:
        Champion.__init__(self, name, race)

    def __str__(self) -> str:
        return f"{self.name}, {self.race}, {self.hp}, {self.manna}, {self.power}, {self.armor}"

    def getRage(self) -> None:
        random: int = random.randint(30, 60)
        
        self.power += random
        self.hp += 120
        self.manna -= 200
        self.armor += 50