l = [2,3,0,5,6,4,2]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            print(f"Číslo {l[i]} se opakuje na indexech {i} a {j}")

