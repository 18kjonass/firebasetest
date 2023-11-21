import serial
from serial.tools import list_ports
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
def doSomething(response):
    print(response.data)

cred = credentials.Certificate("C:/Users/18KJonass.ACC/Downloads/firebasetest-main/firebasetest-main/kristest-f1594-firebase-adminsdk-u2f4b-a9526dbff7.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://kristest-f1594-default-rtdb.europe-west1.firebasedatabase.app/'})

ref= db.reference()
#ref.update({'light_log': ''})
ref = db.reference().child('light_log')
ref.listen(doSomething)
ref.update({str(time.time()):'random'})