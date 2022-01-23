import os
import time

temp: str = "" 
eletkor: int = 0

while(eletkor > 99 and eletkor < 0):
    temp = input("Kérem adjon meg egy életkort, 99 éves korig bezárólag: ")
    if(temp.isnumeric()):
        eletkor = int(temp)
    else:
        print("nem számot adott meg")
        time.sleep(3)
        os.system("cls")

if(eletkor <= 6 and eletkor >= 0):
    print("Gyerek")
elif(eletkor <= 18 and eletkor >= 7):
    print("Iskolás")
elif(eletkor <= 65 and eletkor >= 19):
    print("Dolgozó")
else:
    print("Nyugdíjas")

