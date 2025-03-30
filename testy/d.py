delka1 = int(input("Zadejte délku seznamu: "))
seznam = []
for x in range(delka1):
    seznam.append(int(input(f"Zadej {x + 1} pro první seznam: ")))

delka2 = int(input("Zadejte délku seznamu: "))
seznam2 = []
for y in range(delka2):
    seznam2.append(int(input(f"Zadej {y + 1} pro druhý seznam: ")))


spojeno = []
for i in range(max(delka1, delka2)):
    if(i < delka1):
        spojeno.append(seznam[i])
    if(i < delka2):
        spojeno.append(seznam2[i])

print(spojeno)






