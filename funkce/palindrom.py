def je_palindrom(slovo):
    slovo = slovo.lower()
    if slovo == slovo[::-1]:
        return True
    else:
        return False
    
print(je_palindrom("oko"))  # True
print(je_palindrom("Python"))  # False
print(je_palindrom("Rotor"))  # True

