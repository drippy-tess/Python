class Tulajdonos:
    def __init__(self, nev: str, szuletesiDatum: str, nem: str, szuletesiHely: str) -> None:
        super().__init__()

        self.nev = nev
        self.szuletesiDatum = szuletesiDatum
        self.nem = nem
        self.szuletesiHely = szuletesiHely

    def __str__(self) -> str:
        return f"A motorkerékpár tulajdonosa: {self.nev}\nSzületési helye, ideje: {self.szuletesiHely}, {self.szuletesiDatum}\nNeme: {self.nem}"