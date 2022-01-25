import imp
from re import T
import time
import random
numofbinstrinoneline=int(input("Gimme num of lines: "))
while True:
    binstr=""
    for j in range(numofbinstrinoneline):
        for i in range(8):
            binstr+=random.choice(["0", "1"])
        binstr+=" "
    print(binstr)
    time.sleep(0.05)