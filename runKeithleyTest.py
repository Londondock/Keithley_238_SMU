import time
import serial
import smufunctions


ser = serial.Serial(port='COM3',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

keithley = smufunctions.smu(ser)

keithley.setOperateOnOff(False)
keithley.setSource('sweepcurrent')
#time.sleep(0.1)
#keithley.triggerNow()
#time.sleep(0.1)
keithley.setCompliance(6.000,0)
#time.sleep(0.1)
keithley.setBias(0.5e-9,1,0)
#time.sleep(0.1)
keithley.setLinearSweep(-1.0e-9,1.0e-9,0.1e-9,1,2000)
#time.sleep(0.1)
keithley.setOperateOnOff(True)
#time.sleep(0.1)
keithley.setTriggerNow()
time.sleep(60)
keithley.setDataFormat(15,0,1)
#time.sleep(0.1)

#ser.write('++read \r')
#time.sleep(0.1)
#s = ser.readline()
#print s

count = 0
while count < 21:
    ser.write('++read \r')
    time.sleep(0.1)
    s = ser.readline()
    print s
    count += 1

keithley.setOperateOnOff(False)
ser.close()