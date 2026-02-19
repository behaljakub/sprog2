def vytvor_trojuhelnik(n):
    for x in range(n): # cyklus, ktery urcuje kolikrat se bude opakovat n-1
        for z in range(x): # cyklus zajistujici aby se cyklus opakoval stale i pote co skonci cyklus prvni
            print("*", end = "") # end = "" hvezdicky se budou vypisovat na radek bez mezer
        print("")

print(vytvor_trojuhelnik(5))