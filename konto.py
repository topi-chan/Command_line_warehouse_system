from magazyn_manager import *

manager = Manager()
manager.file_read(sys.argv[1])
print("Stan konta: ", manager.saldo)
