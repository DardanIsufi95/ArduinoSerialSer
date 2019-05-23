import serial
import serial.tools.list_ports
import time

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]

if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

if not arduino_ports:
    print("No Arduino found")
    
ser = serial.Serial(arduino_ports[0])
ser.baudrate = 9200
