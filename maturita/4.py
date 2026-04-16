def je_silne_heslo(heslo):
    seznam = []
    for x in heslo:
        seznam.append(x)
    count1 = 0
    count2 = 0
    count3 = 0
    for x in seznam:
        if x.isupper():
            count1 += 1

        elif x.islower():
            count2 += 1

        elif x.isdigit():
            count3 += 1

    if count1 > 1 and count2 > 1 and count3 > 1:
        return True
            
    else:
        return False
        

print(je_silne_heslo("Heslo123"))    # Očekávaný výstup: True
print(je_silne_heslo("heslo123"))    # Očekávaný výstup: False
print(je_silne_heslo("HESLO123"))    # Očekávaný výstup: False
print(je_silne_heslo("Abc1"))        # Očekávaný výstup: False




    