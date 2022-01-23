import time
import os

a: str = ""
b: str = ""
kezdoErtek: int = 0
vegErtek: int = 0

while(a == None):
    a = input("Kérem adjon meg egy számot: ")
    if(a.isnumeric()):
        kezdoErtek = int(a)
    else:
        print("Nem számot adott meg.")
        time.sleep(2)
        os.system("cls")

while(b < a):
    b = input("Kérem adjon meg egy másik számot: ")
    if(b.isnumeric()):
        vegErtek = int(b)
    else:
        print("Nem számot adott meg.")
        time.sleep(2)
        os.system("cls")

for i in range(vegErtek, kezdoErtek, -1):
    print(f"{i}")