l = [2, 3, 1, 0, 5, 6, 4, 2]
target = (input("Zadej číslo, které chceš najít: "))
misto = []
index = 0

for i in l:
    if i == target:
        misto.append(index)
    index += 1 

print("Číslo", target, "se nachází na indexech:", misto)