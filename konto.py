import sys
import time
from magazyn_manager import *

magazyn = Manager()
(saldo, lista, magazyn) = magazyn.file_read(sys.argv[1])
print("Stan konta: ", saldo)
