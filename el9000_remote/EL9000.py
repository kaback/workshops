import serial

class EL9000Error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class EL9000:

    def __init__(self,comport):
	self.ser = serial.Serial(comport, 9600, parity=serial.PARITY_EVEN)

	if not self.ser.isOpen():
            raise EL9000error('Serial Port could not be opened')

    def decodeAnswer(self,answer):
        h = answer.encode('hex')
        return int(h[4:8], 16)

    def getStatus(self):
        self.ser.write('0248ffff03'.decode('hex')) #status?
        s = self.ser.read(5)
	return self.decodeAnswer(s)

    def setDischargeMode(self):
        self.ser.write('0249000603'.decode('hex'))
        s = self.ser.read(5)
	ans = self.decodeAnswer(s)
	assert ans == 6

        #i_maxh 100ma (10)
        self.ser.write('023C000a03'.decode('hex'))
        s = self.ser.read(5)
	ans = self.decodeAnswer(s)
	assert ans == 10
        
        #0_maxh 1000mV (100)
        self.ser.write('023D006403'.decode('hex'))
        s = self.ser.read(5)
	ans = self.decodeAnswer(s)
	assert ans == 100

    def getMeasData(self):
        self.ser.write('0233000003'.decode('hex'))
        s = self.ser.read(5)
	meas_Ah = self.decodeAnswer(s)
        
        self.ser.write('0232000003'.decode('hex'))
        s = self.ser.read(5)
	meas_mAh = self.decodeAnswer(s)
        
        self.ser.write('0235000003'.decode('hex'))
        s = self.ser.read(5)
	meas_i = self.decodeAnswer(s)
        
        self.ser.write('0234000003'.decode('hex'))
        s = self.ser.read(5)
	meas_u = self.decodeAnswer(s)

        return (meas_Ah, meas_mAh, meas_i, meas_u)

    def loadOn(self):
        self.ser.write('0247000003'.decode('hex')) #status?
        s = self.ser.read(5)
	return self.decodeAnswer(s)

