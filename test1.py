import serial
import time
ser = serial.Serial('COM9',9600,timeout=1)
	
time.sleep(1.5) # can't be <= 1

ser.write('1'.encode())
#print("Hi")

time.sleep(0.5)

ser.write('0'.encode())

#ser.flush() #force the physical write
#print("Hi")
#time.sleep(2) #no need to sleep as flush was blocking

ser.close()