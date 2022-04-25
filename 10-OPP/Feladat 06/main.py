from Szuperhos import Szuperhos

eredmeny: bool = None
szuperhos1: Szuperhos = Szuperhos("Algebrai törtek")
szuperhos2: Szuperhos = Szuperhos("Gyökvonás")

print(szuperhos1)
print(szuperhos2)

eredmeny = szuperhos1.tamad(szuperhos2)
if(eredmeny == True):
    print("Nyert")
else:
    print("Veszített")