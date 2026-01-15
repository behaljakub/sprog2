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


