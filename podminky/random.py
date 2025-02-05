n1 = float(input("Zadejte první číslo: "))
n2 = float(input("Zadejte druhé číslo: "))
n3 = float(input("Zadejte třetí číslo: "))

if n1 >= n1 and n2 >= n3:
    if n2 >= n3:
        print(f"Čísla sestupně: {n1}, {n2}, {n3}")
    else:
        print(f"Čísla sestupně: {n1}, {n3}, {n2}")

elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(f"Čísla sestupně: {n2}, {n1}, {n3}")
    else:
        print(f"Čísla sestupně: {n2}, {n3}, {n1}")