import serial
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
            ser = serial.Serial(p.device , 9200)
            ser.baudrate = 9200
            conn = True
            time.sleep(2)
            print("Connected")

sio = socketio.Client()
sio.connect('http://test-dardan-test.1d35.starter-us-east-1.openshiftapps.com')

l = ""


@sio.on('NTC')
def on_NTC(data):
    d = str(data)
    ser.write(d.encode())
    print(d)


def send_data(data):
    sio.emit('CTN', data)


def ReadSerial(_ser):
    while True:
        reading = _ser.readline().decode("ascii")
        send_data(reading)


thread = threading.Thread(target=ReadSerial, args=(ser,))
thread.start()
