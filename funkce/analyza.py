def analyzuj_text(text):
    vysledek = {
        "pocet_znaku":0,
        "pocet_pismen":0,
        "pocet_slov":0,
        "pocet_vet":0,
        "prumer":0,
        "nejdelsi":"",
        "nejkratsi":"",
    }
    if not text:
        return vysledek
    
    vysledek["pocet_znaku"] = len(text)

    slova = slova.split()

    vysledek["pocet_slov"] = len(slova)

    text = text.replace("!", ".")
    vety = vety.split(".")

    vysledek = ["pocet_vet"] = len(vety)
    vysledek = ["nejdelsi"] = max(slova, key = len)
    vysledek = ["nejkratsi"] = min(slova, key = len)

