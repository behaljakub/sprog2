import math

x = float(input("Zadejte první číslo: "))
y = float(input("Zadejte druhé číslo: "))

if x >= 0 and y >= 0:
    print("Bod A se nachází v I kvadrantu")

elif x <= 0 and y >=0:
    print("Bod A se nachází v II kvadrantu")

elif x <= 0 and y <= 0:
    print("Bod A se nachází v III kvadrantu")

else:
    print("Bod A se nachází v IV kvadrantu")

