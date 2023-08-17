from flask import Flask , render_template ,request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def displayForm():
    return render_template("06_form.html")

@app.route('/result',methods=['POST','GET'])
def displayResult():
    if request.method == 'POST':
        resultData = request.form
        return render_template('06_display_result.html',result = resultData)


if __name__ == '__main__':
    app.run(port = 5000,debug = True)
