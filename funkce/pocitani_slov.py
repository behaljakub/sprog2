def pocitani_slov(text, min_delka=3):
    slovnik = {}
    text = text.lower()
    interpunkce = ".,!?;:"
    for znak in interpunkce:
        text = text.replace(znak, "")


    slova = text.split()
    

    for slovo in slova:
        if len(slovo) >= min_delka:
            if slovo in slovnik:
                slovnik[slovo] += 1
            else:
                slovnik[slovo] = 1
    
    return slovnik

    


print(pocitani_slov("Python je skvělý, Python je mocný programovací jazyk."))

print(pocitani_slov("Ahoj jak se máš", min_delka=4))
