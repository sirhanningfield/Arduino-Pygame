import sys , time
import serial


comport = 'COM5'
b_rate = 9600

arduino = serial.Serial(comport,b_rate,timeout=0)

while True:
	pos = arduino.readline().strip().decode()
	time.sleep(0.3)
	print(pos)

