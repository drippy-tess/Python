from fuggvenyTabla import *
import time
import os

felhasznaloNev: str = None
jelszo: str = None
exist: bool = None

felhasznaloNev = emailBekeres()
jelszo = jelszoBekeres()
exist = isUserExists(felhasznaloNev, jelszo)

if(exist == True):
    print("Sikeres bejelentkezés a rendszerbe!")
else:
    print("A rendszerhez való hozzáférés megtagadva!")
    time.sleep(3)
    os.system("cls")