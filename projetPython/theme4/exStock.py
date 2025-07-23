def calcul_stock(n):
    stock = 1024
    stocks = [stock]
    for semaine in range(2, n + 1):
        stock -= (20 + semaine)
        if semaine % 4 == 0:
            stock += 500
        stocks.append(stock)
    return stocks

while True:
    print("\na. Prévisions de stock")
    print("b. Stock maximal")
    print("(q pour quitter)")
    choix = input().strip()

    if choix == 'q':
        break

    elif choix == 'a':
        n = int(input("Choisissez une semaine : "))
        stocks = calcul_stock(n)
        for i, s in enumerate(stocks, start=1):
            print(f"Semaine {i} : stock {s}")

    elif choix == 'b':
        n = int(input("Choisissez une semaine : "))
        stocks = calcul_stock(n)
        max_stock = max(stocks)
        semaine_max = stocks.index(max_stock) + 1
        print(f"Stock max égal à {max_stock} , atteint en semaine {semaine_max}")

    else:
        while choix not in ('a', 'b', 'q'):
            print("Choix incorrect, recommencez", end=" ")
            choix = input().strip()
            if choix == 'q':
                break
            elif choix == 'a' or choix == 'b':
                break