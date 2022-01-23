print("x= ")
x: float = float(input())

print("y= ")
y: float = float(input())

print("z= ")
z: float = float(input())

print("k= ")
k: float = float(input())

osszeg: float = x + y

kulonbseg: float = z - k

eredmeny: float = osszeg / kulonbseg

print(f"({x} + {y}) / ({z} - {k}) = {eredmeny}")