def nejdelsi_slovo(text):
    slova = text.split()
    nejdelsi = ""
    for slovo in slova:
<<<<<<< HEAD
        if len(slovo) > len(nejdelsi):
            nejdelsi = slovo
    return nejdelsi

print(nejdelsi_slovo("Včera jsme šli na výlet do hor"))
=======
        if len(nejdelsi) < len(slovo):
            nejdelsi = slovo
    return nejdelsi
        
print(nejdelsi_slovo("Včera jsme šli na výlet do hor"))
>>>>>>> 0cbd7734e9ef775e9bd514923953d86545b53097
