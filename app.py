from flask import Flask , render_template ,  request
from flask_mail import Mail , Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'preetiharjani1382@gmail.com'
app.config['MAIL_PASSWORD'] = 'Preetiharjani6352'
mail = Mail(app)


@app.route('/' , methods=["GET" , "POST"])
def home():
    if request.method == "POST" : 
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('msg')

        msg = Message(
            subject = f"mail from {name}" , 
            body = f" Name : {name} \n Email : {email} \n\n Message : \n {message}" , 
            sender = 'preetiharjani1382@gmail.com' , recipients = ['harjanipreeti63@gmail.com']
        )
        mail.send(msg)
    
    return render_template('index.html')


if(__name__ == '__main__') : 
    app.run(debug=True)