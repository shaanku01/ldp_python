from flask import Flask , render_template , request , redirect  , url_for , flash

app = Flask(__name__)
app.secret_key("This is unique")

@app.route("/")
def index():
    return render_template('10_flashing_index.html')

@app.route('/login',methods=["POST","GET"])
def login():
    error = None
    if(request.method == "POST"):
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = "Invalid user name or password"
        else:
            flash("You have logged in successfully")
            flash("donot forget to logoff before you go!")
            return redirect(url_for('index'))
    return render_template("10_login_template.html" , error = error)

if __name__ == '__main__':
    app.run(port = 5000,debug = True)


"""
Syntax of flash:

Flask.flash(message,category)


TO remove the flashed messages from a session:
we can use the get_flashed_messages() function..

the flashed messages will be generated at 1 view function and passed on to the next one.
the next one will have template and the flash messages can be collected from that template.

"""


