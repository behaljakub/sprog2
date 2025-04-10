def nejdelsi_slovo(text):
    slova = text.split()
    nejdelsi = ""
    for slovo in slova:
        if len(nejdelsi) < len(slovo):
            nejdelsi = slovo
    return nejdelsi
        
print(nejdelsi_slovo("Včera jsme šli na výlet do hor"))