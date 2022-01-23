import os
import time

valasztas: int = None
temp: str = ""

print("1 - Coca Cola")
print("2 - Pepsi Cola")
print("3 - Sprite")
print("4 - Fanta")
print("5 - Mountain Dew")
time.sleep(2)

while(valasztas == None):
    temp = input("Kérem válasszon üdítőt: ")
    if(temp.isdigit()):
        valasztas = int(temp)
    else:
        print("Nem megfelelő bevitel!")
        time.sleep(3)
        os.system("cls")

    if(valasztas == 1):
        print("Köszönjük a vásárlást! Te a Coca Cola-t választottad.")
    elif(valasztas == 2):
        print("Köszönjük a vásárlást! Te a Pepsi Cola-t választottad.")
    elif(valasztas == 3):
        print("Köszönjük a vásárlást! Te a Sprite-ot választottad.")
    elif(valasztas == 4):
        print("Köszönjük a vásárlást! Te a Fanta-t választottad.")
    elif(valasztas == 5):
        print("Köszönjük a vásárlást! Te a Mountain Dew-t választottad.")
    else:
        print("Nem a választékból választott!")

time.sleep(3)
os.system("cls")