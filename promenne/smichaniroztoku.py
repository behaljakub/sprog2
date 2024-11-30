import math

v1 = float(input("Objem prvního roztoku (v ml): "))
k1 = float(input("Koncentrace prvního roztoku (v %): "))
v2 = float(input("Objem druhého roztoku (v ml): "))
k2 = float(input("Koncentrace druhého roztoku (v %): "))

celkk = (v1*k1)+(v2*k2)/v1+v2

print(f"Koncentrace výsledného roztoku: {celkk} %")
