from champion import Champion
import random

class Orc(Champion):
    def __init__(self, name: str, race: str) -> None:
        Champion.__init__(self, name, race)

    def __str__(self) -> str:
         return f"{self.name}, {self.race}, {self.hp}, {self.manna}, {self.power}, {self.armor}"
    
    def letsMakeTrouble(self) -> None:
        random: int = random.randint(20, 50)
        
        self.power += random
        self.hp += 200
        self.manna -= 150
        self.armor += 40