import sys

class Manager():
    """Warehouse management system"""

    def __init__(self):
        self.saldo = 0
        self.lista = []
        self.magazyn = {}
        self.actions = None

    def file_read(self, fhand):
        fhand = open(fhand)
        while True:
            fh = fhand.readline().strip()
            if fh.startswith("saldo"):
                self.lista.append(fh)
                money = fhand.readline().strip()
                com = fhand.readline().strip()
                self.saldo += int(money)
                self.lista.append(money)
                self.lista.append(com)
            if fh.startswith("zakup"):
                name = fhand.readline().strip()
                price = int(fhand.readline().strip())
                pieces = int(fhand.readline().strip())
                self.zakup(name, price, pieces)
            if fh.startswith("sprzedaż"):
                self.lista.append(fh)
                name = fhand.readline().strip()
                if name in self.magazyn:
                    self.sprzedaz(name, price, pieces)
                else:
                    print("Brak takiego produktu w magazynie")
                    quit()
            if fh == "":
                return (self.saldo, self.lista, self.magazyn)

    def file_write(self, fname, lista):
        fd = open(fname, "w")
        for element in self.lista:
            fd.write(str(element))
            fd.write("\n")

    def assign(self, name, qty):
        def decorator(cb):
            self.actions[name] = (cb, qty)
        return decorator

    def review(self):
        saldo = 0
        lista = []
        magazyn = {}
        index = -1
        fhand = open(sys.argv[1])
        while True:
            y = int(sys.argv[2])
            z = int(sys.argv[3])
            fh = fhand.readline().strip()
            if fh.startswith("saldo"):
                money = fhand.readline().strip()
                com = fhand.readline().strip()
                saldo += int(money)
                index += 1
                if index >= y and index <= z:
                    lista.append(fh)
                    lista.append(money)
                    lista.append(com)
                fh
            if fh.startswith("zakup"):
                name = fhand.readline().strip()
                price = int(fhand.readline().strip())
                if price < 0:
                    print("Błąd - cena nie może być mniejsza od zera")
                    quit()
                pieces = int(fhand.readline().strip())
                if pieces < 0:
                    print("Błąd - liczba sztuk nie może być mniejsza od zera")
                    quit()
                if (price * pieces) <= saldo:
                    magazyn[name] = magazyn.get(name, 0) +pieces
                    saldo -= (price * pieces)
                    index += 1
                    if index >= y and index <= z:
                        lista.append(fh)
                        lista.append(name)
                        lista.append(price)
                        lista.append(pieces)
                    fh
                else:
                    print("Błąd - brak wystarczającej ilości środków na koncie")
                    quit()
            if fh.startswith("sprzedaż"):
                name = fhand.readline().strip()
                if name in magazyn:
                    price = int(fhand.readline().strip())
                    if price < 0:
                        print("Błąd - cena nie może być mniejsza od zera")
                        quit()
                    pieces = int(fhand.readline().strip())
                    if pieces < 0:
                        print("Błąd - liczba sztuk nie może być mniejsza od zera")
                        quit()
                    if (price * pieces) <= saldo:
                        magazyn[name] = magazyn.get(name, 0) -pieces
                        saldo -= (price * pieces)
                        index += 1
                        if index >= y and index <= z:
                            lista.append(fh)
                            lista.append(name)
                            lista.append(price)
                            lista.append(pieces)
                        fh
                    else:
                        print("Błąd - brak wystarczającej ilości środków na koncie")
                        quit()
                else:
                    print("Brak takiego produktu w magazynie")
                    quit()
            if fh.startswith("stop"):
                break
        for element in lista:
            print(element)
