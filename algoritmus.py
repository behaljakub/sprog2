cisla = [5, 1, 4, 8, 2, 3]

for x in range(len(cisla)):
    for i in range(len(cisla)-1):
        if cisla[x] > cisla[x+1]:
            nahrazene = cisla[x]
            cisla[x+1] = cisla[x]
            cisla = nahrazene

print(cisla)
    



