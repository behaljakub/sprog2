def nejdelsi_slovo(text):
    seznam_slov = text.split()
    nejdelsi = seznam_slov[0]
    for x in seznam_slov:
        if x < nejdelsi:
            nejdelsi = x
    return nejdelsi


def nejdelsi_slovov2(text):
    slova = text.split()
    return max(slova, key=len)

print(nejdelsi_slovov2("Včera jsme šli na výlet do hor"))


