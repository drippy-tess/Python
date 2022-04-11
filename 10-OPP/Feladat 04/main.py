from Tanulo import Tanulo
from Osztaly import Osztaly

tanulo: Tanulo = Tanulo("Kedd", "Krisztián", "2000. január 1.")
tanulo1: Tanulo = Tanulo("Szerda", "Szabolcs", "2001. február 2.")
tanulo2: Tanulo = Tanulo("Csütörtök", "Csaba", "2002. március 3.")
osztaly: Osztaly = Osztaly("10.B", tanulo, tanulo1, tanulo2)

print(osztaly)