def do_dvojkove(n):

    vysledek = " "

    while n > 0:
        vysledek = str(n%2) + vysledek
        n = n//2

    return vysledek

do_dvojkove(5)
do_dvojkove(10)
