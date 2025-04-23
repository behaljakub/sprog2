def nejdelsi_slovo(text):
    seznam_slov = text.split()
    nejdelsi = seznam_slov[0]
    for x in seznam_slov:
        if x < nejdelsi:
            nejdelsi = x
    return nejdelsi

print(nejdelsi_slovo("Včera jsme šli na výlet do hor"))  # "Včera"