from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/hello/<name>')
def helloName(name):
    return "Hello {0}".format(name)

if __name__ == '__main__':
    app.run(port = 4300,debug = True)


"""
Script Notes:

1. debug = True : no need to restart server, can directly make changes and save, it will reflect.

2. @app.route('/') is a decorater, '/' on trigerring the specified route the below method will be executed.

3. __name__ is the name of the module.

4. app.run() has 4 parameters - app.run(host,port,debug,options)

5. if debug mode is not activated the service can be made available to other users by setting host
to '0.0.0.0'.

6. Line - 9 decorator with the ability to handle path variables.

"""

