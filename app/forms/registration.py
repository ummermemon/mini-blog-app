from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField,EmailField
from wtforms.validators import DataRequired,Email

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={'placeholder': 'Enter First Name'})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={'placeholder': 'Enter Last Name'})
    email = EmailField('Email', validators=[DataRequired()], render_kw={'placeholder': 'Enter Email '})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Enter Password'})
    signup = SubmitField('Sign Up')
