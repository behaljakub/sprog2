def soucet(lst):
    if lst == []:
        return 0

    return lst[0] + soucet(lst[1:])