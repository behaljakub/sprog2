import math

class zlomek:
    def __init__(self, citatel, jmenovatel=1):
        self.citatel = citatel
        self.jmenovatel = jmenovatel
        pass
    
    def __str__(self):
        return f"{self.citatel}/{self.jmenovatel}"

    def zkrat(self):
        nsd = math.gcd(abs(self.citatel), abs(self.jmenovatel))
        self.citatel //= nsd
        self.jmenovatel //= nsd
        return self
        
    def __add__(self, jiny):
        novy_citatel = self.citatel*jiny.jmenovatel + self.jmenovatel*jiny.citatel
        novy_jmenovatel = self.jmenovatel*jiny.jmenovatel
        vysledek = zlomek(novy_citatel, novy_jmenovatel)

        return vysledek.zkrat()
    
    def __sub__(self, jiny):
        novy_citatel = self.citatel*jiny.jmenovatel - self.jmenovatel*jiny.citatel
        novy_jmenovatel = self.jmenovatel*jiny.jmenovatel
        vysledek = zlomek(novy_citatel, novy_jmenovatel)

        return vysledek.zkrat()
    
    def __mul__(self, jiny):
        novy_citatel = self.citatel*jiny.citatel
        novy_jmenovatel = self.jmenovatel*jiny.jmenovatel
        vysledek = zlomek(novy_citatel, novy_jmenovatel)

        return vysledek.zkrat()
    
    def __truediv__(self, jiny):
        novy_citatel = self.citatel*jiny.jmenovatel
        novy_jmenovatel = self.jmenovatel*jiny.citatel
        vysledek = zlomek(novy_citatel, novy_jmenovatel)

        return vysledek.zkrat()
    

 
# Test 1: Vytvoření zlomků
z1 = zlomek(1, 2)
z2 = zlomek(3, 4)
z3 = zlomek(5)
print(f"z1 = {z1}")  # 1/2
print(f"z2 = {z2}")  # 3/4
print(f"z3 = {z3}")  # 5/1

# Test 2: Sčítání
print(f"{z1} + {z2} = {z1 + z2}")  # 5/4

# Test 3: Odčítání
print(f"{z2} - {z1} = {z2 - z1}")  # 1/4

# Test 4: Násobení
print(f"{z1} * {z2} = {z1 * z2}")  # 3/8

# Test 5: Dělení
print(f"{z1} / {z2} = {z1 / z2}")  # 2/3

# Test 6: Složitější výpočet
print(f"({z1} + {z2}) * {z3} = {(z1 + z2) * z3}")  # 25/4

# Test 7: Zkracování
z4 = zlomek(8, 12)
print(f"Před zkrácením: {z4}")  # 8/12
z4.zkrat()
print(f"Po zkrácení: {z4}")    # 2/3

