class Ssd:
    def __init__(self, gyarto: str, tipus: str, meret: int):
        super().__init()
        
        self.gyarto = gyarto
        self.tipus = tipus
        self.meret =meret
        
    def​ ​__str__​(​self​) ​->​ ​str​: 
 ​        ​return​ ​f"Az SSD típusa és gyártója: ​{​self​.gyarto}​ {self.tipus}\n​Mérete: ​{​self​.​meret}​GB"