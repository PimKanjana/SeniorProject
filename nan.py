from nanpy import*
connection = SerialManager(device='COM7')
a = ArduinoApi(connection=connection)
a.pinMode(13,a.OUTPUT)
#a.digitalWrite(13,a.HIGH)

a.digitalWrite(13,a.LOW)
a.pinMode(13,a.OUTPUT)