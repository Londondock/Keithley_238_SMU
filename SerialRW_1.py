import time
import serial

def main():
    # configure the serial connections (the parameters depend on your device)
    ser = serial.Serial(
        port='COM3',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    
    # ser.open()
    ser.isOpen()
    
    print 'Enter your commands below.\r\nInsert "exit" leave the application.'
    
    input=1
    while 1 :
            # get keyboard input
        input = raw_input(">> ")
            # Python 3 users
            # input = input(">> ")
        if input == 'exit':
            ser.close()
            break
        else:
            # send the character to the device
            # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
            ser.write(input + '\r\n')
            out = ''
            # let's wait before reading output (let's give device time to answer)
            time.sleep(0.1)
            #ser.write('++read \r')
            time.sleep(0.1)
            while ser.inWaiting() > 0:
                out += ser.read(1)
    
            if out != '':
                print ">>" + out

if __name__ == '__main__':
    main()