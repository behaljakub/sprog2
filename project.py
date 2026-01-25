import math

class Zlomek:
    def __init__(self, citatel, jmenovatel=1):
        self.citatel = citatel
        self.jmenovatel = jmenovatel

    def __str__(self):
        return (f"{self.citatel}/{self.jmenovatel}")
    
    def zkrat(self):
        nsd = math.gcd(abs(self.citatel), abs(self.jmenovatel))
        print(nsd)
        self.citatel//nsd
        self.jmenovatel//nsd
        return self
    
z4 = Zlomek(8, 12)
print(f"Před zkrácením: {z4}")  # 8/12
z4.zkrat()
print(f"Po zkrácení: {z4}") 
    

    



