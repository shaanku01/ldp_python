from flask import Flask , session , request , render_template , redirect , url_for

app = Flask(__name__)
app.secret_key = "This is unique"

@app.route('/')
def index():
    if "username" in session:
        username = session['username']
        return 'Logged in as {0} <br>'.format(username) + "<b><a href='/logout'>click here to logout</a></b>"
    else:
        return "You are not logged in : <a href='/login'>click here to login</a>"
    
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index'))
    else:
        return render_template("08_session_form.html")
    
@app.route('/logout')
def logout():
    # Remove user name from session if it is there
    session.pop('username',None)
    return redirect(url_for('index'))    

if __name__ == "__main__":
    app.run(port = 5000,debug = True)

"""
    session key is required to perform encryption.

    session is the period of time the user loggs in to the server to the time the user loggs out.
    
    session object can be imported from the flask framework and be utilised.
    

"""
