c1 = float(input("Zadejte první stranu: "))
c2 = float(input("Zadejte druhou stranu: "))
c3 = float(input("Zadejte třetí stranu: "))

if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
    if c1 == c2 == c3:
        print(f"Strany {c1}, {c2}, {c3} tvoří rovnostranný trojúhelník")

    elif c1 == c2 or c1 == c3 or c2 == c3:
        print("Trojúhelník je rovnoramenný")
    
    else:
        print("Trojúhelník je obecný")
else:
    print("Strany netvoří trojúhelník")


if c1**2 == c2**2 + c3**2 or c3**2 == c1**2 - c2**2 or c2**2 == c1**2 - c3**2:
    print("Trojúhelník je pravoúhlý")
elif c1**2 > c2**2 + c3**2 or c2**2 > c1**2 + c3**2 or c3**2 > c2**2 + c1**2:
    print("Trojúhelník je topoúhly")
else:
    print("Trojuhelník je ostroúhlý")








    



