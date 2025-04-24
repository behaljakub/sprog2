def prevod_na_minuty(hodiny, minuty):

    if not isinstance(hodiny, int) or not isinstance(minuty, int):
        return None

    elif  hodiny > 0 and minuty > 0:
        return 60*hodiny + minuty
    else:
        return None
    
print(prevod_na_minuty(2, 45))
print(prevod_na_minuty(-1, 30))
print(prevod_na_minuty(1, -10))
print(prevod_na_minuty(12.6, 2))
