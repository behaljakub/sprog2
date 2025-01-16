mez = int(input("Napiš mez: "))
cislo = 0
for cislo in range(1, mez+1):
    if cislo%2 == 0:
        print(f"Číslo {cislo} je sudé") 
        cislo = 1
    else:
        print(f"Číslo {cislo} je liché")
        
