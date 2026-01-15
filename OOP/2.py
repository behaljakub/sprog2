import math

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
    def __add__(self, jiny):
        x_souradnice = self.x + jiny.x
        y_souradnice = self.y + jiny.y
        return Vektor(self.x + jiny.x, self.y + jiny.y)
    
    def __sub__(self, jiny):
        x_souradnice = self.x - jiny.x
        y_souradnice = self.y - jiny.y
        return Vektor(self.x - jiny.x, self.y - jiny.y)
    
    def delka(self):
        return math.sqrt((self.x)**2 + (self.y)**2)
    
    def __mul__(self, jiny):
        if isinstance(jiny, Vektor):
            return self.x*jiny.x + self.y*jiny.y
        
        elif isinstance(jiny, (int, float)):
            return Vektor(jiny*self.x, jiny*self.y)
        
# Test 1: Vytvoření vektorů
v1 = Vektor(3, 4)
v2 = Vektor(1, 2)
print(f"v1 = {v1}")  # [3, 4]
print(f"v2 = {v2}")  # [1, 2]
# Test 2: Sčítání
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")  # [3, 4] + [1, 2] = [4, 6]
# Test 3: Odčítání
v4 = v1 - v2
print(f"{v1} - {v2} = {v4}")  # [3, 4] - [1, 2] = [2, 2]
# Test 4: Délka
print(f"Délka {v1} = {v1.delka()}")  # 5.0
# Test 5: Skalární součin
skalarni = v1 * v2
print(f"{v1} · {v2} = {skalarni}")  # 11
# Test 6: Násobení číslem
v5 = v1 * 2
print(f"{v1} * 2 = {v5}")  # [3, 4] * 2 = [6, 8]
# Test 7: Složitější výpočet
v6 = (v1 + v2) * 0.5
print(f"({v1} + {v2}) * 0.5 = {v6}")  # [2.0, 3.0]

        