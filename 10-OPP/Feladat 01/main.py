from Teglalap import Teglalap
from Kor import Kor
from Derekszogu import Derekszogu
from Egyenloszaru import Egyenloszaru
from Egyelooldalu import Egyelooldalu

#példányosítás
teglalap: Teglalap = Teglalap(10, 20)
print(teglalap)

negyzet: Teglalap = Teglalap(10, 10)
print(negyzet)

korKerulet: Kor = Kor(20)
print(korKerulet)

korTerulet: Kor = Kor(10)
print(korTerulet)

derekszoguHaromszog: Derekszogu = Derekszogu(8, 10, 15)
print(derekszoguHaromszog)

egyenloszaruHaromszog: Egyenloszaru = Egyenloszaru(5, 10, 10)
print(egyenloszaruHaromszog)

egyelooldaluHaromszog: Egyelooldalu = Egyelooldalu (10, 10, 10)
print(egyenlooldaluHaromszog)