from flask import Flask , render_template, request, make_response , session , redirect , url_for 
import os
from flask_mail import Mail , Message

app=Flask(__name__)

mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rudrapratapsingh2026@cs.ajce.in'
app.config['MAIL_PASSWORD'] = '********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

@app.route('/')

def index():
    msg = Message('Hello', sender = 'xyz@gmail.com', recipients = ['abc@gmail.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)
    