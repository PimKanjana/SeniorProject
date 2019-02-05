import time
import serial

#ser = serial.Serial('COM3')
ser = serial.Serial(port='COM3', baudrate=115200, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

'''
if ser.isOpen():
    ser.close()
	ser.open()
	ser.isOpen()
''' 

ser.write("!G 1 -300\r".encode())


out = ''
# let's wait one second before reading output (let's give device time to answer)


time.sleep(1)
print(ser.inWaiting())
print(ser.read(5))


while ser.inWaiting() > 0:
	out = out + ser.read(2)
	print(out)
	if out != '':
		print(">>" + out)

ser.close()
