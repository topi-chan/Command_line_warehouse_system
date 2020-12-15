import time, sys

class Manager():
    """Warehouse management system"""

    def __init__(self):
        self.saldo = 0
        self.lista = []
        self.magazyn = {}
        self.nowa_lista = []

    def file_read(self, fhand):
        fhand = open(fhand)
        while True:
            fh = fhand.readline().strip()
            # print(fh)
            # time.sleep(1)
            if fh.startswith("saldo"):
                self.lista.append(fh)
                money = fhand.readline().strip()
                com = fhand.readline().strip()
                self.saldo += int(money)
                self.lista.append(money)
                self.lista.append(com)
                fh
            if fh.startswith("zakup"):
                self.lista.append(fh)
                name = fhand.readline().strip()
                price = int(fhand.readline().strip())
                if price < 0:
                    print("Błąd - cena nie może być mniejsza od zera")
                    quit()
                pieces = int(fhand.readline().strip())
                if pieces < 0:
                    print("Błąd - liczba sztuk nie może być mniejsza od zera")
                    quit()
                if (price * pieces) <= self.saldo:
                    self.lista.append(name)
                    self.lista.append(price)
                    self.lista.append(pieces)
                    self.magazyn[name] = self.magazyn.get(name, 0) +pieces
                    self.saldo -= (price * pieces)
                    fh
                else:
                    print("Błąd - brak wystarczającej ilości środków na koncie")
                    quit()
            if fh.startswith("sprzedaż"):
                self.lista.append(fh)
                name = fhand.readline().strip()
                if name in self.magazyn:
                    price = int(fhand.readline().strip())
                    if price < 0:
                        print("Błąd - cena nie może być mniejsza od zera")
                        quit()
                    pieces = int(fhand.readline().strip())
                    if pieces < 0:
                        print("Błąd - liczba sztuk nie może być mniejsza od zera")
                        quit()
                    if (price * pieces) <= self.saldo:
                        self.lista.append(name)
                        self.lista.append(price)
                        self.lista.append(pieces)
                        self.magazyn[name] = self.magazyn.get(name, 0) -pieces
                        self.saldo -= (price * pieces)
                        fh
                    else:
                        print("Błąd - brak wystarczającej ilości środków na koncie")
                        quit()
                else:
                    print("Brak takiego produktu w magazynie")
                    quit()
            if fh.startswith("stop"):
                return (self.saldo, self.lista, self.magazyn)
                break

    def file_write(self, fname, lista):
        fd = open(fname, "a")
        for element in self.nowa_lista:
            fd.write(str(element))
            fd.write("\n")

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
