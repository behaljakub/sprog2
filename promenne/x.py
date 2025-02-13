soucet = 0
soucetmocnin = 0

for x in range(1,101):
    soucet+=x
    soucetmocnin += x**2

msoucet = soucet**2

print(msoucet - soucetmocnin)
