from flask import Flask , url_for , redirect

app = Flask(__name__)

@app.route('/admin')
def adminRoute():
    return " Hello Admin!!"

@app.route('/guest/<guestName>')
def helloGuest(guestName):
    return "Hello {0}".format(guestName)

@app.route("/user/<name>")
def helloUser(name):
    if name == 'admin':
        return redirect(url_for('adminRoute'))
    else :
        return redirect(url_for('helloGuest',guestName = name))

if __name__ == '__main__':
    app.run(port = 4300,debug = True)

"""
Script Notes:

1.  url_for : this function when given the function name, 
    it finds the associated url for the function

2.  redirect , this function redirects to the particular provided url.

"""