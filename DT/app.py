from flask import Flask, render_template, request, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/message', methods=['GET','POST'])
def message():
    if request.method=='POST':
        print(request.form)
        account_sid = 'ACa5997b07b01460fe7c9f6c12e245f6aa'
        auth_token ='a38790762b7300278f9457bbd3eed07e'
        twilio_number = '+13854583426'
        target_number = '+918925192504'
        client=Client(account_sid,auth_token)
        client.messages.create(
            
            body=f"Amount:{request.form} ",
            from_=twilio_number,
            to=target_number
        )
        
    return redirect(url_for("/"))
        

if __name__ == "__main__":
    app.run(debug=True, port=4000)