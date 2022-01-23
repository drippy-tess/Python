# pip3 install keyboard

# csomagok importálása
import os
#import keyboard
import time

#változók definiálása

# a szám amit be kell olvasni
    # kezdőértéke a None, mivel a while ciklusban ki tudom ezt használni az simétlések vizsgálatára,
    # vagyis a ciklust mindaddig futtatjuk, míg a number változónak nem lesz szám értéke
number: int = None
    # segédváltozó, a beolvasott értéket fogja tárolni
data: str = ""

# while ciklus, ami mindaddig fog futni míg a number változó nem kap szám értéket,
# azaz az értéke nem None lesz
while(number == None):
    data = input("Kerem a szamot: ")
    # megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható-e
    # mindegy, hogy ez a szám int vagy float típusú
    # isdigit() -> bool változót ad vissza
    if(data.isdigit()):
        # ha az isdigit() fügvény értéke igaz, akkor számot írt be a felhasználó
        # amit mit BIZTOS át tudunk szám típussá alakítani
        number = int(data)
        # ha az isdigit() függvény értéke hamis, azaz a felhasználó nem számot írt be
        # így a number változó értéke továbbra is None marad, azaz a felhasználó nem számot írt be
        # a ciklust ismételni kell
    else:
        print("\nNem szamot adott meg!")
        # a programot futtató szálat (thread) elaltatjuk 3 másodpercre
        time.sleep(3)
        # letöröljük a képernyőt
        os.system("cls")
        
        #print("\n A folyatatashoz nyomja meg az ENTER billenyűt.")
            # egy végtelen WHILE ciklust írunk, mivel arra fogunk várni, hogy a felhasználó
            # lenyomja a kért billentyűt (ENTER)
        #while(True):
            # figyeljük, hogy a felhasználó lenyomta-e az ENTER gombot
        #   if(keyboard.is_pressed('enter')):
        #       os.system("cls")
                # kilépünk a belső (végtelen) while ciklusból
        #       break

# kiírjuk a beolvasott számot
print(f"A beolvasott szam: {number}")