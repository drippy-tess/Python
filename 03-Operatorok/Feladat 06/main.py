print("x= ")
x: float = float(input())

print("y= ")
y: float = float(input())

print("z= ")
z: float = float(input())

osszeg: float = x + 0.5

kulonbseg: float = y - 0.7

szorzat: float = osszeg * kulonbseg

maradek: float = szorzat % z

print(f"({osszeg} * {kulonbseg}) % {z} = {maradek}")