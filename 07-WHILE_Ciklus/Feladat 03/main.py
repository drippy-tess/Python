import random

rnd: int = random.randint(0, 9)
tipp: int = int(input("Adja meg a tippjét: "))
tippekSzama: int = 1
temp: str = ""

while(tipp != rnd and tippekSzama <= 5):
    temp = ""
    while(temp == "" or temp.isspace() or not temp.isdigit()):
        temp = input(f"Kérem a {tippekSzama}. tippet: ")
        if(temp.isdigit()):
            tipp = int(temp)
            tippekSzama += 1
        else:
            print("Nem számot adott meg!")

if(tipp == rnd):
    print(f"Gratulálunk, eltalálta a számot: {rnd}.")
else:
    print(f"Sajnos nem találta el a számot: {rnd}.")