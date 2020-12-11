import sys
import time
from magazyn import file_read, file_write

(saldo, lista, magazyn) = file_read(sys.argv[1])
dodanie = int(sys.argv[2])
komentarz = sys.argv[3]
saldo += dodanie
lista.append(dodanie)
lista.append(komentarz)

file_write(sys.argv[1], lista)
