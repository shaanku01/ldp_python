from flask import Flask , render_template , request , redirect , abort , url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("09_redirects_and_errors.html")

@app.route('/login' , methods=["POST","GET"])
def login():
    if request.method == "POST":
        if request.form['username'] == 'admin':
            return redirect('/home')
        else:
            return abort(401)        
    else:
        return redirect(url_for('index'))

@app.route('/home')
def home():
    return '<h1>Welcome to Home Page !</h1>'

if __name__ == '__main__':
    app.run(port = 5000,debug = True)


"""
Flask.abort(code):

codes - 
400 Bad Request: Used when the client's request is malformed or invalid.

401 Unauthorized: Indicates that the client's request lacks proper authentication credentials.

403 Forbidden: Denotes that the client does not have permission to access the requested resource.

404 Not Found: Used when the requested resource could not be found on the server.

500 Internal Server Error: Indicates a generic error message for unexpected server conditions.

"""