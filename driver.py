import serial.tools.list_ports
import time
import threading
import socketio


conn = False
ser = serial.Serial
while not conn:
    print("Waiting for Device...")
    time.sleep(1.5)
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "85632313039351B02110" == p.serial_number:
            ser = serial.Serial(p.device , 9600)
            conn = True
            time.sleep(2)
            print("Connected")



sio = socketio.Client()
sio.connect('http://test-arduino-test.1d35.starter-us-east-1.openshiftapps.com')


@sio.on('NTC')
def on_NTC(data):
    d = str(data)
    ser.write(d.encode())
    print(d)


def send_data(data):
    sio.emit('CTN', data)



def SreialRead():
    while 1:
        if ser.in_waiting:
            reading = ser.readline().decode().rstrip()
            print(reading)
            send_data(reading)

thread = threading.Thread(target=SreialRead())
thread.start()

