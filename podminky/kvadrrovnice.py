import math

a = float(input("Koeficient a: "))
b = float(input("Koeficient b: "))
c = float(input("Koeficient c: "))

D = b**2 - 4*a*c
x1 = (-b + D**0.5)/2*a
x2 = (-b - D**0.5)/2*a

if D > 0:
    print(f"Kořeny rovnice jsou {x1}, {x2}")

elif D == 0:
    print(f"Rovnice má jedno řešení {x1}")

else:
    D < 0
    print("Kořeny rovnice nejsou definovány")



