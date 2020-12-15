import sys
import time
from magazyn_manager import *


manager = Manager()
(saldo, lista, magazyn) = manager.file_read(sys.argv[1])
dodanie = int(sys.argv[2])
komentarz = sys.argv[3]
saldo += dodanie
lista.append(dodanie)
lista.append(komentarz)

manager.file_write(sys.argv[1], lista)
