from Tulajdonos import Tulajdonos

class Motorkerekpar:
    def __init__(self, gyarto: str, tipus: str, kivitel: str, teljesitmeny: int, suly: int, kobcenti: int, tulaj: Tulajdonos) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipus = tipus
        self.kivitel = kivitel
        self.teljesitmeny = teljesitmeny
        self.suly = suly
        self.kobcenti = kobcenti
        self.tulaj = tulaj

    def __str__(self) -> str:
        return f"A motor gyártója: {self.gyarto}\nTípusa: {self.tipus}\nKivitele: {self.kivitel}\nTeljesítménye: {self.teljesitmeny}KW\nSúlya: {self.suly}KG\nHengerűrtartalma: {self.kobcenti}cc\n{self.tulaj}"

