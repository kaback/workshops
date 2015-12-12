from EL9000 import *
from time import sleep,time
import sys

el9000 = EL9000('/dev/ttyS0')
assert el9000.getStatus() == 0

el9000.setDischargeMode()
el9000.loadOn()

while(True):
    sleep(5)
    
    status = el9000.getStatus() #ladeschluss?
    (Ah, mAh, i, u) = el9000.getMeasData()
    timestamp = int(time())
    array = [timestamp, Ah, mAh, i, u, status]

    print ','.join(map(str,array)) 
    sys.stdout.flush()
    assert status != 8
