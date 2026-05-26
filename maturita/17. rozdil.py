def rozdil_mocnin(n):
    soucet_mocnin = 0
    for x in range(1, n+1):
        soucet_mocnin += x
    druha_mocnina_souctu = soucet_mocnin**2
    
    soucet_druhe_mocniny = 0
    for i in range(1, n+1):
        soucet_druhe_mocniny += i*i

    soucet = druha_mocnina_souctu - soucet_druhe_mocniny

    return soucet

print(rozdil_mocnin(10))    # → 2640
print(rozdil_mocnin(100))   # → 25164150
print(rozdil_mocnin(1))     # → 0