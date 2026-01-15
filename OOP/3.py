class Barva:
    def __init__(self, r, g, b):
        if r > 255 or g > 255 or b > 255:
            return "ValueError (Hodnoty RGB musí být 0-255)"
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"

    def __add__(self, jina):
        nova_r = (self.r + jina.r)//2
        nova_g = (self.g + jina.g)//2
        nova_b = (self.b + jina.b)//2
        return Barva(nova_r, nova_g, nova_b)
    
    def __mul__(self, nasobek):
        nova_r = int(self.r*nasobek)
        nova_g = int(self.g*nasobek)
        nova_b = int(self.b*nasobek)
        nova_r = max(0, min(255, int(self.r * nasobek))) #pouziti v prvnim kroku?
        nova_g = max(0, min(255, int(self.g * nasobek)))
        nova_b = max(0, min(255, int(self.b * nasobek)))
        return Barva(nova_r, nova_g, nova_b)
    
    def invertuj(self):
        nova_r = 255 - self.r
        nova_g = 255 - self.g
        nova_b = 255 - self.b
        return Barva(nova_r, nova_g, nova_b)
    
    def to_hex(self):
        self.r = "RR"
        self.g = "GG"
        self.b = "BB"
        return f"{self.r}{self.g}{self.b}"
    
oranzova = Barva(255, 100, 0)
print(f"{oranzova} = {oranzova.to_hex()}")  
# RGB(255, 100, 0) = #FF6400
bila = Barva(255, 255, 255)
print(f"{bila} = {bila.to_hex()}")  
# RGB(255, 255, 255) = #FFFFFF