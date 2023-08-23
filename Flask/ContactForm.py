# from flask_wtf import Form
# from wtforms import StringField , IntegerField , TextAreaField , SubmitField , RadioField , SelectField

# from wtforms import validators , ValidationError

# class ContactForm(Form):
#     name = StringField("Name of the Student", [validators.DataRequired("please Enter your name")])
#     Gender = RadioField("Gender",choices=[('M','Male'),('F','Female')])
#     Address = TextAreaField('Address')

#     email = StringField("Email",[validators.DataRequired("Please Enter your Email address"), validators.Email("Please enter your email correctly")])

#     Age = IntegerField("age")
#     language = SelectField('Languages',choices=[('cpp','C++'),('py','Python')])
#     submit  = SubmitField("Send")

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name of the Student", [DataRequired("Please enter your name")])
    Gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField('Address')
    email = StringField("Email", [DataRequired("Please enter your email address"), Email("Please enter a valid email address")])
    Age = IntegerField("Age")
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")

