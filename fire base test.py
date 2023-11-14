import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#change this to the path of the private key you downloaded
cred = credentials.Certificate("C:/Users/krist/Downloads/kristest-f1594-firebase-adminsdk-u2f4b-a9526dbff7")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://kristest-f1594-default-rtdb.europe-west1.firebasedatabase.app/'})

#get a reference to our db
ref = db.reference('/')
'''
the / is referencing the root of our database - the very start
lets try and add some data
we need to use a dictionary
'''
ref.set({'users': {'user1':{'name':'kris',
                            'height':'super tall',
                            'age':18},
                   
                   'user2':{'name':'zack',
                            'height':'super small',
                            'age':17},
    }})
#the dictionary goes in {}, a {} inside a {} is a nested dictionary