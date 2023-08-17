from flask import Flask , url_for , redirect , request

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcomeMessage(name):
    return " Welcome {0}".format(name)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        # request.form['nm']  
        username = request.form.get('nm')            
        return redirect(url_for('welcomeMessage',name = username))
    else:
        username = request.args.get('nm')
        return redirect(url_for('welcomeMessage',name = username))
    
if __name__ == '__main__':
    app.run(port = 4300,debug = True)


"""
        # Access form data using request.form
        username = request.form.get('nm')  # Assuming 'nm' is the name attribute in your form
        print("Form Data:", request.form)
        
        # Access query parameters using request.args
        query_parameters = request.args
        print("Query Parameters:", query_parameters)
        
        # Access headers using request.headers
        headers = request.headers
        print("Headers:", headers)
        
        # Access cookies using request.cookies
        cookies = request.cookies
        print("Cookies:", cookies)



        The output you provided, ImmutableMultiDict([('nm', 'Shanker')]),
        indicates that you've printed the contents of the request.
        form object after submitting a form with the field "nm" containing the value "Shanker".


        So, when you access request.form.get('nm'), 
        you're retrieving the value associated with the key "nm" from the form data.

"""