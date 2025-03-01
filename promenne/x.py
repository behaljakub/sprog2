soucet = 0
soucetmocnin = 0

for x in range(1,101):
    soucet+=x

for y in range(1,101):
    soucetmocnin += x*x

msoucet = soucet**2

print(msoucet - soucetmocnin)
