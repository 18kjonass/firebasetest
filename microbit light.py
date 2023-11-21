import serial
from serial.tools import list_ports
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1


def find_comport(pid, vid, baud):
    """returns a serial port"""
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    # scanning ports
    print("Scanning Ports...")
    for p in ports:
        try:
            print(f'Testing: \n\t port: {p!r} \n\t pid: {p.pid} \n\t vid: {p.vid}')
        except AttributeError:
            continue

        if p.pid == pid and p.vid == vid:
            print(f'found target device: \n\t pid: {p.pid} \n\t vid: {p.vid} \n\t port: {p.device}')
            ser_port.port = str(p.device)
            return ser_port
    return None

ser = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
ser.open()

#change this to the path of the private key you downloaded
cred = credentials.Certificate("C:/Users/18KJonass.ACC/Downloads/firebasetest-main/firebasetest-main/kristest-f1594-firebase-adminsdk-u2f4b-a9526dbff7.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://kristest-f1594-default-rtdb.europe-west1.firebasedatabase.app/'})

#get a reference to our db
ref= db.reference()
ref.update({'light_log': ''})
ref = db.reference().child('light_log')
#Where is this temperature originating from source
#input("Please input the source of this data: ")


while True:
    #read and decode the input
    mb_light = str(ser.readline().decode('utf-8'))
    #clean up the input
    mb_light = mb_light.replace(" ","")
    mb_light = mb_light.replace("\r\n","")
    #make sure it is only numbers we are logging as temperature
    
    if mb_light.isdigit():
        print(mb_light)
        ref.update({str(int(time.time())):{'Light': mb_light}})
        
    
        
