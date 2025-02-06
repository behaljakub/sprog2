c1 = int(input("Zadejte první stranu: "))
c2 = int(input("Zadejte druhou stranu: "))
c3 = int(input("Zadejte třetí stranu: "))

if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
    if c1 == c2 == c3:
        print(f"Strany {c1}, {c2}, {c3} tvoří rovnostranný trojúhelník")
    
    elif c1 == c2 or c1 == c3 or c2 == c3:
        print(f"Strany {c1}, {c2}, {c3} tvoří rovnoramenný trpjúhelník")
    
    else:
        print(f"Strany {c1}, {c2}, {c3} tvoří obecný trojúhelník")

    
    
