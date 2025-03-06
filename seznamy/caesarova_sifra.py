text = str(input("Zadejte text: "))
key = int(input("Zadejte posun: "))

abc = ['a', "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "r", "s", "t", "u", "v", "x", "y", "z"]

vysledek = []

for x in range(len(text)):
    if x in abc:
        for i in range(len(abc)):
            if x == abc[(i+key)%len(abc)]:
                text += vysledek

prevod_na_string = "".join(vysledek)

print(str(prevod_na_string))


#desifrace





