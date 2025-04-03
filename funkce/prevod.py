def prevod_na_minuty(hodiny, minuty):
    if  hodiny > 0 and minuty:
        return 60*hodiny + minuty
    else:
        return None
    
print(prevod_na_minuty(2, 45))
print(prevod_na_minuty(-1, 30))
