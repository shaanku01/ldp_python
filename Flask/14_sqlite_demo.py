from flask import Flask , render_template , request , redirect , url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('14_home.html')

@app.route('/enternew')
def new_student():
    return render_template('14_student.html')

@app.route("/db-setup")
def setDataBase():
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        addr TEXT,
        city TEXT,
        pin TEXT
        );
        '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/addrec' , methods=["POST","GET"])
def addrec():
    if request.method == "POST":
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pinCode = request.form['pin-code']

            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(name,address,city,pinCode))
                con.commit()
                msg = "Record added successfully"
        except:
            con.rollback()
            msg = "error in operation"

        finally:
            con.close()
            return render_template("14_result.html",msg = msg)
        
@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template("14_list.html",rows=rows)

if __name__ == '__main__':
    app.run(debug = True)


"""

Sqllite3 is a python build in library which provides a database support.

this code provides a basic functionality of adding sudents to database and retreiving them 
and displaying them on templates.

"""