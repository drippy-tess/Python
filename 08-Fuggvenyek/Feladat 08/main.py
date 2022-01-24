import time
import os

pont: int = None
osztalyzat: int = None

#Hiba
def hiba(uzenet:str) -> None:
    print(uzenet)
    time.sleep(2)
    os.sytem("cls")

#Pontszám bekérése
def pontszamBekeres() -> int:
    pontSzam: int = None
    data: str = None
    
    while(pontSzam == None):
        data = input("Kérem adja meg a pontszámot! \n")
        if(data.isdigit() and int(data) >= 0 and int(data) <= 100):
            pontSzam = int(data)
            return pontSzam
        else:
            hiba("Helytelen bevitel!")

#Pontszám vizsgálata
def pontszamVizsgalat(szam:int) -> int:
    if(szam < 50):
        return 1
    elif(szam >= 50 and szam < 60):
        return 2
    elif(szam >= 60 and szam < 70):
        return 3
    elif(szam >= 70 and szam < 85):
        return 4
    else:
        return 5

#Kiírás
def kiiras(pontSzam:int, erdemjegy:int) -> None:
    print(f"Ön elért {pontSzam} pontot, ami {erdemjegy} osztályzatot eredményez!")
    time.sleep(5)
    os.system("cls")

#Főprogram
pont = pontszamBekeres()
osztalyzat = pontszamVizsgalat(pont)
kiiras(pont, osztalyzat)