from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def renderTemplate():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(port = 4300,debug = True)



"""
render_template function  will go to the templates folder and get the required template
and render it.
"""