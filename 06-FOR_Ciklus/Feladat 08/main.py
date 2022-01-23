print("Adja meg a kezdő értéket!")
kezdoErtek: int = int(input())

print("Adja meg a végértéket!")
vegErtek: int = int(input())

if (kezdoErtek % 2 == 0):
    kezdoErtek += 1
    
for i in range(kezdoErtek, vegErtek, 2):
    print(i)