import sys
import time
from magazyn import file_read, file_write

(saldo, lista, magazyn) = file_read(sys.argv[1])
nazwanie = sys.argv[2]
ceny = int(sys.argv[3])
sztuki = int(sys.argv[4])
saldo += ceny*sztuki
lista.append(nazwanie)
lista.append(ceny)
lista.append(sztuki)

file_write(sys.argv[1], lista)
