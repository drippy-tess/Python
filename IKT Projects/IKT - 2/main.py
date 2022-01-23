sorok: int = int(input("Kérem adja meg hány elemű a számpiramis!"))

x = 0
szamolo = 0
szamolo1 = 0

for i in range(1, sorok+1, 1):
    for space in range(1, (sorok-i)+1):
        print("  ", end="")
        szamolo+=1
    
    while x!=((2*i)-1):
        if szamolo<=sorok-1:
            print(i+x, end=" ")
            szamolo+=1
        else:
            szamolo1+=1
            print(i+x-(2*szamolo1), end=" ")
        x += 1
    
    szamolo1 = szamolo = x = 0
    print()