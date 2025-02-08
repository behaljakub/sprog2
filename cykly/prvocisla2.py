cislo = int(input("Zadejte přirozené prvočíslo: "))

delitel = 0

for x in range(1, cislo + 1):
    if cislo%x == 0:
        delitel += 1
    
if delitel == 2:
    print(f"Číslo {cislo} je prvočíslo")
else:
    print("Číslo není prvočíslo")