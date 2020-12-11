import time

class Manager():
    """Warehouse management system"""

    def __init__(self):
        self.saldo = 0
        self.lista = []
        self.magazyn = {}

    def file_read(fhand):
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

    def file_write(fname, lista):
        fd = open(fname, "a")
        for element in self.lista:
            fd.write(str(element))
            fd.write("\n")
        fd.write("stop")
