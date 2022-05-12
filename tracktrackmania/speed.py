# this must be run as admin
# the memory address is set at startup

from pymem import Pymem

pm = Pymem('TmForever.exe')
while True:
    value = pm.read_int(0x10338B44)
    print(value)