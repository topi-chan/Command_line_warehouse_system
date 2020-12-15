import sys
import time
from magazyn_manager import *

manager = Manager()
manager.file_read(sys.argv[1])
for arg in sys.argv[2:]:
    print(arg, manager.magazyn[arg])
