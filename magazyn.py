import sys
import time
from magazyn import file_read

(saldo, lista, magazyn) = file_read(sys.argv[1])
for arg in sys.argv[2:]:
    print(arg, magazyn[arg])
