import sys
import time
from magazyn_manager import *

#po co zwracam listę? tam już sprawdziłem, a tutaj nadpisuje się dwukrotnie w pliku
manager = Manager()
manager.file_read(sys.argv[1])
manager.saldo += int(sys.argv[2])
manager.nowa_lista.append(int(sys.argv[2]))
manager.nowa_lista.append(sys.argv[3])
manager.file_write(sys.argv[1], manager.nowa_lista)
