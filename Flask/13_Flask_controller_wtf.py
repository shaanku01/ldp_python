from flask import Flask , render_template , request , flash

from ContactForm import ContactForm

app = Flask(__name__)
app.secret_key = "Development Key"

@app.route('/contact',methods=["GET","POST"])
def contact():
    form = ContactForm()

    if request.method == "POST":
        if list(form.errors.items()) !=  []:
            flash('All fields are required')
            return render_template('13_contact.html', form = form)
        else:
            return render_template('13_success.html')
        
    if request.method == 'GET':
        return render_template('13_contact.html' , form = form)
    
if __name__ == '__main__':
    app.run(debug = True)