from magazyn_manager import *

def manager_create():
    manager = Manager()
    @manager.assign("zakup", 3)
    def manager_buy(manager, name, price, pieces):
        price = int(price)
        pieces = int(pieces)
        if price < 0:
            print("Błąd - cena nie może być mniejsza od zera")
            quit()
        if pieces < 0:
            print("Błąd - liczba sztuk nie może być mniejsza od zera")
            quit()
        if (price * pieces) <= manager.saldo:
            manager.lista.append("zakup")
            manager.lista.append(name)
            manager.lista.append(price)
            manager.lista.append(pieces)
            manager.magazyn[name] = manager.magazyn.get(name, 0) +pieces
            manager.saldo -= (price * pieces)
        else:
            print("Błąd - brak wystarczającej ilości środków na koncie")
            quit()
    @manager.assign("sprzedaż", 3)
    def manager_sell(manager, name, price, pieces):
        price = int(price)
        pieces = int(pieces)
        if name in manager.magazyn:
            if price < 0:
                print("Błąd - cena nie może być mniejsza od zera")
                quit()
            if pieces < 0:
                print("Błąd - liczba sztuk nie może być mniejsza od zera")
                quit()
            if (price * pieces) <= manager.saldo:
                manager.lista.append("sprzedaż")
                manager.lista.append(name)
                manager.lista.append(price)
                manager.lista.append(pieces)
                manager.magazyn[name] = manager.magazyn.get(name, 0) -pieces
                manager.saldo -= (price * pieces)
            else:
                print("Błąd - brak wystarczającej ilości środków na koncie")
                quit()
        else:
            print("Brak takiego produktu w magazynie")
            quit()
    @manager.assign("saldo", 2)
    def manager_balance(manager, money, commentary):
        manager.lista.append("saldo")
        manager.saldo += int(money)
        manager.lista.append(money)
        manager.lista.append(commentary)
    @manager.assign("konto", 0)
    def manager_balance(manager):
        pass
    return manager
