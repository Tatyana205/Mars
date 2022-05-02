from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, EmailField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    email = EmailField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('r_password', message='Пароли должны совпадать')])
    r_password = PasswordField('Repeat password')
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
