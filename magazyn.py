import sys
import time
from magazyn_manager import *

magaz = Manager()
(saldo, lista, magazyn) = magaz.file_read(sys.argv[1])
for arg in sys.argv[2:]:
    print(arg, magazyn[arg])
