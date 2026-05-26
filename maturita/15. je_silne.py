def je_silne_heslo(heslo):

    for x in heslo:
        count_velke = 0
        count_male = 0
        count_digit = 0
        count_znak = 0
        for x in heslo:
            count_znak += 1
            if x.isupper():
                count_velke += 1
            elif x.islower():
                count_male += 1
            elif x.isdigit():
                count_digit += 1
 
        if count_velke and count_male and count_digit >= 1 and count_znak >= 8:
            return True
        else:
            return False
print(je_silne_heslo('Heslo123'))   # → True
print(je_silne_heslo('heslo123'))   # → False  (chybí velké písmeno)
print(je_silne_heslo('HESLO123'))   # → False  (chybí malé písmeno)
print(je_silne_heslo('Abc1'))       # → False  (příliš krátké)
