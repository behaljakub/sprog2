mez = 10000

pi = 1

for k in range (1, mez+1):
    pi *= (4*k**2)/(4*k**2 - 1)

pi_value = 2*pi

pi_value = round(pi, 3)

print(f"{pi_value}")