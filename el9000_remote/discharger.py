from EL9000 import *
from time import sleep

el9000 = EL9000('/dev/ttyS0')
assert el9000.getStatus() == 0

el9000.setDischargeMode()
el9000.loadOn()

while(True):
    sleep(5)
    
    status = el9000.getStatus() #ladeschluss?
    (Ah, mAh, i, u) = el9000.getMeasData()
    array = [Ah, mAh, i, u, status]

    print ','.join(map(str,array)) 
    assert status != 8
