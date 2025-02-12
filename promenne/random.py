cislo = int(input("Zadejte číslo: "))

if cislo < 2:
    print(f"{cislo} není prvočíslo")

else:
    cislo2 = cislo
    delitel = 0

    for x in range(1, cislo + 1):
        if cislo2%x == 0:
            delitel +=1

    if delitel == 2:
      print(f"{cislo2} je prvočíslo")
    else:
      print(f"{cislo2} není prvočíslo")
    