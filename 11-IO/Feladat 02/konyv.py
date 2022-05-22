class Konyv:
    def __init__(self, vezNev: str, kerNev: str, szulDatum: str, cim: str, isbn: int, kiado: str, kiadasiev: str, ar: int, tema: str, oldalSzam: int, honorarium: int) -> None:
        super().__init__()

        self.vezNev = vezNev
        self.kerNev = kerNev
        self.szulDatum = szulDatum
        self.cim = cim
        self.isbn = isbn
        self.kiado = kiado
        self.kiadasiev = kiadasiev
        self.ar = ar
        self.tema = tema
        self.oldalSzam = oldalSzam
        self.honorarium = honorarium

    def __str__(self) -> str:
        return f"{self.vezNev} {self.kerNev} {self.szulDatum} {self.cim} {self.isbn} {self.kiado} {self.kiadasiev} {self.ar} {self.tema}, {self.oldalSzam} {self.honorarium}"