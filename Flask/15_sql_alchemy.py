from flask import Flask , request , flash , url_for , redirect , render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tuser:root@localhost:5432/college'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column('student_id',db.Integer,primary_key = True , autoincrement=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    address = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self,id,name,city,address,pin):
        self.id = id
        self.name = name
        self.city = city
        self.address = address
        self.pin = pin

@app.route('/')
def show_all():    
    return render_template('15_show_all.html' , students = students.query.all())

@app.route('/new' , methods=["POST" , "GET"])
def new():
    if request.method == 'POST':
        if not request.form["name"] or not request.form['city'] or not request.form['address']:
            flash("Please enter all the fields")
        else:
            student = students(random.randint(1, 10000),request.form['name'],request.form['city'],request.form['address'],request.form['pin'])
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('show_all'))
    return render_template('15_new_student.html')


if __name__ == '__main__':
    app.run(debug = True)