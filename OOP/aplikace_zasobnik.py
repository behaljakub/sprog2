from zasobnik2 import *

zasobnik = Stack()

data = input("Zadejte mat. operaci: ")

def zkontroluj_zavorky(data):
    for char in data:
        if char == "(":
            zasobnik.push(char)

        elif char == ")":
            last_item = zasobnik.peek()
            if last_item == "(":
                zasobnik.pop()
            else:
                return False
    
    if zasobnik.IsEmpty():
        return True
    else:
        return False