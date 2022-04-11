class Tanulo:
    def __init__(self, vezetknev: str, keresztnev: str, szuletesiDatum: str) -> None:
        super().__init__()

        self.vezetknev: str = vezetknev
        self.keresztnev: str = keresztnev
        self.szuletesiDatum: str = szuletesiDatum

    def __str__(self) -> str:
        return f"A tanuló vezetékneve, majd keresztneve: {self.vezetknev} {self.keresztnev}, Születési dátuma: {self.szuletesiDatum}"