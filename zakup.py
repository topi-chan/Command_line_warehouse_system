from magazyn_manager import *

manager = Manager()
manager.file_read(sys.argv[1])
manager.zakup(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
manager.file_write(sys.argv[1], manager.nowa_lista)
