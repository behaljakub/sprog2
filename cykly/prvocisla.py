c = int(input("Zadejte přirozené číslo: "))

if c < 2:
    print(f"Číslo {c} není prvočíslo")
else:
    delitel = 0
    for x in range(1, c + 1):
        if c % x == 0:
            delitel += 1

    if delitel == 2:
        print(f"Číslo {c} je prvočíslo")
    else:
        print(f"Číslo {c} není prvočíslo")




