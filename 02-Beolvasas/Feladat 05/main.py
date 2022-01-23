print("Kérem adja meg kedvenc filmének címét!")
kedvencFilm: str = str(input())

print("Kérem adja meg a megjelenés évét!")
megjelenesiEv: int = int(input())

print("Kérem adja meg a film rendezőjének nevét!")
rendezoNev: str = str(input())

print("Kérem adja meg a főszereplőjének nevét!")
foszereploNev: str = str(input())

print(f"{megjelenesiEv}-ban/ben {rendezoNev} rendezésében megjelent a/az {kedvencFilm} című film {foszereploNev} főszereplésével.")