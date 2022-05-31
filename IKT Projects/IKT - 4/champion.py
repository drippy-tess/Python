import random

class Champion:
    def __init__(self, name: str, race: str) -> None:
        super().__init__()

        self.name: str = name
        self.race: str = race
        self.hp: int = random.randint(500, 800)
        self.manna: int = random.randint(600 ,750)
        self.power: int = random.randint(1000, 2000)
        self.armor: int = random.randint(400, 800)

    def __str__(self) -> str:
        return f"{self.name}, {self.race}, {self.hp}, {self.manna}, {self.power}, {self.armor}"

    def attack(self, enemy: "Champion") -> bool:
        return (self.power > enemy.armor)

    def condition(self) -> bool:
        return (self.hp > 0 and self.manna > 0)