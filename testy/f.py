import random

def uziv_slovo(slovo):
    znaky = []
    for znak in slovo:
        znaky += [znak]



    for x in range (len(znaky)):
        poz1 = random.randint(0, len(slovo) - 1)
        poz2 = random.randint(0, len(slovo) - 1)

        a = znaky[poz1]
        b = znaky[poz2]

        znaky[poz1] = b
        znaky[poz2] = a

    nove_slovo = ""
    for y in znaky:
        nove_slovo += y
    
    return nove_slovo

slovo = input("Zadej slovo:")


print(uziv_slovo(slovo))


