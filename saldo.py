# from magazyn_manager import *
#
# manager = Manager()
# manager.file_read(sys.argv[1])
# manager.saldo += int(sys.argv[2])
# manager.nowa_lista.append("saldo")
# manager.nowa_lista.append(int(sys.argv[2]))
# manager.nowa_lista.append(sys.argv[3])
# manager.file_write(sys.argv[1], manager.nowa_lista)
from mg import manager_create
import sys

manager = manager_create()
manager.file_read(sys.argv[1])
