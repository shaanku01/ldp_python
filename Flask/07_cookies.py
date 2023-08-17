from flask import Flask , render_template , request , make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('07_display_form_for_cookies.html')

@app.route('/cookie-link',methods=["POST","GET"])
def setCookie():
    if request.method == 'POST':
        user = request.form['username']
        resp = make_response(render_template("07_read_cookie.html"))
        resp.set_cookie('UserId',user)
        return resp

@app.route('/get-cookie')
def getCookie():
    name = request.cookies.get('UserId')
    return '<h1>welcome {0}</h1>'.format(name)


if __name__ == '__main__':
    app.run(port = 5000,debug = True)

"""
Main demo in this code is the make_response() function

this function gives the instance of the response object.
where we can modify the properties of reponse object.



"""