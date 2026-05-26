def delitelna(x,n):
    for i in range(1, n+1):
        if i%x == 0:
            print(i, end=" ")
    print()

delitelna(3, 10)    # → '3 6 9'
delitelna(5, 20)    # → '5 10 15 20'
delitelna(2, 10)    # → '2 4 6 8 10'