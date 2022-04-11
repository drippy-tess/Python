class Jatekosok:
    def __init__(self, vezetknev: str, keresztnev: str, mezSzam: int, poszt: str) -> None:
        super().__init__()

        self.vezetknev: str = vezetknev
        self.keresztnev: str = keresztnev
        self.mezSzam: int = mezSzam
        self.poszt: str = poszt

    def __str__(self) -> str:
        return f"A játékos vezetékneve, keresztneve: {self.vezetknev} {self.keresztnev}, Mezszáma: {self.mezSzam}, Posztja: {self.poszt}"