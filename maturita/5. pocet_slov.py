def pocet_slov(text):

    mezera = False
    pocet = 0
    for x in text:
        if x != " " and not mezera:
            pocet +=1
            mezera = True
        elif x == " ":
            mezera = False
            
    return pocet

print(pocet_slov('Ahoj světe'))   # → 2
print(pocet_slov('Python'))        # → 1
print(pocet_slov(''))              # → 0
print(pocet_slov('  ahoj  '))      # → 1