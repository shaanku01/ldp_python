from flask import Flask , render_template , request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('11_upload_file.html')

@app.route('/uploader' , methods=["POST","GET"])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
    
if __name__ == '__main__':
    app.run(debug=True)


"""
FILE UPLOAD ACTIVITY:


f.save(secure_filename(f.filename)): will save the file to the server temporarily

"""
