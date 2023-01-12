import firebase_admin
from datetime import date
from twilio.rest import Client
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
result=db.collection("UserRemainder").stream()
list=[]
for doc in result:
    dict=doc.to_dict()
    list.append(dict)
print(list)

for i in list:
    today=date.today()
    if(str(today)==i["Date"]):
        account_sid = 'ACa472bb316876a31e7155af195ab0757a'
        auth_token ='6d44ecbdb5702c125fead760bb45757c'
        twilio_number = '+15044147359'
        target_number = '+91'+str(i["Phone"])
        client=Client(account_sid,auth_token)
        client.messages.create(
        body=str(i["Remainder"]),
        from_=twilio_number,
        to=target_number
)