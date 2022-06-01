class Roplabda:
    def __init__(self, nev: str, magassag: int, poszt: str, nemzetiseg: str, csapat: str, orszag: str) -> None:
        super().__init__()

        self.nev = nev
        self.magassag = magassag
        self.poszt = poszt
        self.nemzetiseg = nemzetiseg
        self.csapat = csapat
        self.orszag = orszag

    def __str__(self) -> str:
        return f"{self.nev} {self.magassag} {self.poszt} {self.nemzetiseg} {self.csapat} {self.orszag}"