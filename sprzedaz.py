import sys
import time
from magazyn_manager import *

manager = Manager()
(saldo, lista, magazyn) = manager.file_read(sys.argv[1])
nazwanie = sys.argv[2]
ceny = int(sys.argv[3])
sztuki = int(sys.argv[4])
lista.append(nazwanie)
lista.append(ceny)
lista.append(sztuki)
print(lista)

manager.file_write(sys.argv[1], lista)
