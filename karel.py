import random



def hadej_cislo():
    cislo = random.randint(1, 100)
    print(cislo)
    pokusy = 10

    while pokusy > 0:
        n = int(input("Zadejte hádené číslo: "))
        pokusy -= 1

        if n < cislo:
            return "Higher"
        
        elif n > cislo:
            return "Lower"
        
        elif cislo == n:
            return "Vyhrál jsi"
        
        else:
            return "Došli ti pokusy, zkus to znovu"
        
hadej_cislo()
        