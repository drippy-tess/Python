from sys import int_info
from typing import *
import random
from Jatekos import Jatekos

tippek: Set[int] = (5, 98, 45, 67, 98, 76)
kihuzott: Set[int] = set()
jatekos1: Jatekos = Jatekos("Kiss János", tippek)

while(len(kihuzott) < 6):
        kihuzott.add(random.randint(1, 99))

print(jatekos1)
print(f"Kihúzott számok:{kihuzott}")

jo = jatekos1.talalt(kihuzott)
print(f"Eltalált számok: {len(jo)}")