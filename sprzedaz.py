from magazyn_manager import *

manager = Manager()
manager.file_read(sys.argv[1])
manager.nowa_lista.append("sprzedaż")
manager.nowa_lista.append(sys.argv[2])
manager.nowa_lista.append(int(sys.argv[3]))
manager.nowa_lista.append(int(sys.argv[4]))
manager.file_write(sys.argv[1], manager.nowa_lista)
