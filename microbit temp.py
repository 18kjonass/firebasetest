import serial
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

ser = serial.Serial()
#change on local 
ser.baubrate = 115200
ser.port = "COM5"
ser.open()

#change this to the path of the private key you downloaded
cred = credentials.Certificate("C:/Users/krist/Downloads/kristest-f1594-firebase-adminsdk-u2f4b-a9526dbff7")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://kristest-f1594-default-rtdb.europe-west1.firebasedatabase.app/'})

#get a reference to our db
ref= db.reference()
ref.update({'temperature_log': ''})
ref = db.reference().child('temperature_log')
#Where is this temperature originating from
source input("Please input the source of this data: ")
i = 0

while True:
    #read and decode the input
    mb_temperature = str(ser.readline().decode('utf-8'))
    #clean up the input
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\n","")
    #make sure it is only numbers we are logging as temperature
    if mb_temperature.isdigit():
        ref.update({str(int(time.time())):{'Temperature' : mb_temperature, 'Location': source}})
        i = i+1
    else:
