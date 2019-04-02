import serial 
ser = serial.Serial('COM3')
#ser = serial.Serial(port='COM3', baudrate=115200, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
print(ser.name)
#print(ser.write(b'hello'))
print(ser.write("!G 1 500".encode()))

ser.close()
print(ser.is_open)