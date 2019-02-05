import serial 
ser = serial.Serial('COM3')
print(ser.name)
#print(ser.write(b'hello'))
print(ser.write("!G 1 500".encode()))

ser.close()
print(ser.is_open)