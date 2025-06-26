from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()], render_kw={'placeholder': "Enter Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': "Enter Password"})
    login = SubmitField('Login')