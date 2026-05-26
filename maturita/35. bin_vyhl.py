def binarni_vyhledavani(lst, cil):
    if len(lst) == 0:
        return False

    if lst[0] == cil:
        return True

    return binarni_vyhledavani(lst[1:], cil)


# Příklad použití
print(binarni_vyhledavani([1, 3, 5, 7, 9], 5))  # True
print(binarni_vyhledavani([1, 3, 5, 7, 9], 4))  # False