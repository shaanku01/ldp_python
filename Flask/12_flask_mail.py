from flask import Flask
from flask_mail import Mail , Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'xyz@gmail.com'
app.config['MAIL_PASSWORD'] = '****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/send-mail')
def index():
    msg = Message("Hello", sender='xyz@gmail.com' , recipients=['abc@gmail.com'])
    msg.body = "Hello Flask! This message is sent from Shanker's Flask Application"
    mail.send(msg)
    return 'Message Sent'

if __name__ == '__main__':
    app.run(debug=True)