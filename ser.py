import serial
import time

ser = serial.Serial('COM9',9600)
#ser = serial.Serial(port='COM7', baudrate=9600, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
time.sleep(2)
#print("What!")
#print(ser.readline())
#print("Enter 1 to turn LED ON and 0 to turn LED OFF")

while 1:
	'''
	#print("the")
	var = input()
	print("you entered", var)
	
	if(var == '1'):
		ser.write('1'.encode())
		print("LED turned ON")
		#time.sleep(1)
	if(var == '0'):
		ser.write('0'.encode())
		print("LED turned OFF")
	'''
	ser.write('1'.encode())
	time.sleep(500)