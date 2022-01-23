hatarErtek: int = 0
probakSzama: int = 0
osszeg: int = 0
szam: int = 0
szam1: int = 0

while(hatarErtek < 100):
    hatarErtek: int = int(input("Kérem adja meg a határértéket: "))
    szam: int = int(input("Kérem adjon meg egy számot: "))
    osszeg = szam

while (osszeg < 100):
    szam1: int = int(input("Írjon be egy másik számot: "))
    osszeg = osszeg + szam1
    probakSzama += 1
    print(f"{osszeg}")
    print(f"A próbálkozások száma: {probakSzama}.")

print(f"A {hatarErtek} számot {probakSzama} próbálkozásból érte el.")