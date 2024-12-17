cislo1 = float(input("Zadejte první čislo: "))
cislo2 = float(input("Zadejte druhé čislo: "))
cislo3 = float(input("Zadejte třetí číslo: "))

if cislo1 >= cislo2 and cislo1 >= cislo3:
    if cislo2 >= cislo3:
        sestupne = (cislo1, cislo2, cislo3)
    else:
        sestupne = (cislo1, cislo3, cislo2)

elif cislo2 >= cislo1 and cislo2 >= cislo3:
    if cislo1 >= cislo3:
        sestupne = (cislo2, cislo1, cislo3)
    else:
        sestupne = (cislo2, cislo3, cislo1)

else:
    if cislo1 >= cislo2:
        sestupne = (cislo3, cislo1, cislo2)
    else:
        sestupne = (cislo3, cislo2, cislo1)

print(f"Čísla seřazena sestupně:{sestupne}")
    
