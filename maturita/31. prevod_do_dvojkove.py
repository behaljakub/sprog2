def do_dvojkove(n):
    string = " "
    while n > 0:
        vysledek = n%2
        string = str(vysledek) + string
        n//=2
    print(string)


do_dvojkove(5)    # → '101'

