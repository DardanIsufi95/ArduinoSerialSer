import serial
import serial.tools.list_ports
import time
import threading
import socketio


def connect():
	arduino_ports = [
		p.device
		for p in serial.tools.list_ports.comports()
		if 'Arduino' in p.description
	]

	if len(arduino_ports) > 1:
		print('Multiple Arduinos found - using the first')

	if not arduino_ports:
		print("No Arduino found")
		time.sleep(1.5)
		connect()

connect()
ser = serial.Serial(arduino_ports[0])
ser.baudrate = 9200
ser.open()

sio = socketio.Client()
sio.connect('http://test-dardan-test.1d35.starter-us-east-1.openshiftapps.com')	

l = ""

@sio.on('NTC')
def on_NTC(data):
	d = str(data)
	if(d != l)
		l = d
		ser.write(d.encode())
		print(d)
		
		

		
		
		
def send_data(data)
	if(len(data) == 12)
	sio.emit('CTN' , data)

def ReadSerial(ser):
	while True:
		reading = ser.readline().decode()
		send_data(reading)


thread = threading.Thread(target=ReadSerial, args=(ser))
thread.start()
