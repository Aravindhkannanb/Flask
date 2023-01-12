import json
import firebase_admin
from datetime import date
from twilio.rest import Client
from firebase_admin import credentials
from firebase_admin import firestore
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["UserTransactionDetails"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
result=db.collection("UserTransactiondetails").stream()
list=[]
for doc in result:
    dict=doc.to_dict()
    write_json(dict)

