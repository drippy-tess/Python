class Levelezesicim:
    def __init__(self, telepules: str, iranyitoszam: int, megye: str, kozterulet: str, szam: int) -> None:
        super().__init__()

        self.telepules: str = telepules
        self.iranyitoszam: int = iranyitoszam
        self.megye: str = megye
        self.kozterulet: str = kozterulet
        self.szam: int = szam

    def __str__(self) -> str:
        return f"Levelezési címe: {self.megye}, {self.iranyitoszam} {self.telepules}, {self.kozterulet} {self.szam}."