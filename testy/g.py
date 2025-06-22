def spocitej_slova(veta: str):
    nova_veta = veta.split(" ")
    interpunkce = ".,!?;:"
    for znak in interpunkce:
        text = veta.replace(znak, "")

    pocet_slov = len(text)

    return print(pocet_slov)


print(spocitej_slova("Červená kočka běžela přes louku."))
