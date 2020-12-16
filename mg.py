def manager_create():
    manager = Manager()
    @manager.assign("zakup", 3)
    def manager_buy(manager, name, price, pieces):
        manager.lista.append("zakup")
        price = int(price)
        if price < 0:
            print("Błąd - cena nie może być mniejsza od zera")
            quit()
        price = int(price)
        if pieces < 0:
            print("Błąd - liczba sztuk nie może być mniejsza od zera")
            quit()
        if (price * pieces) <= manager.saldo:
            manager.lista.append(name)
            manager.lista.append(price)
            manager.lista.append(pieces)
            manager.magazyn[name] = manager.magazyn.get(name, 0) +pieces
            manager.saldo -= (price * pieces)
        else:
            print("Błąd - brak wystarczającej ilości środków na koncie")
            quit()
    @manager.assign("saldo", 2)
        def manager_balance(xxxx,,x,x):
