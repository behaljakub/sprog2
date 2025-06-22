cisla = {}

def fib(n):
    if n in cisla:
        return cisla[n]
    if n == 0:
        cisla[n] = 0
    elif n == 1:
        cisla[n] = 1
    else:
        cisla[n] = fib(n - 1) + fib(n - 2)
    return cisla[n]

print(fib(1))

