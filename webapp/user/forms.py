from flask_wtf import FlaskForm # we need it for creating a form
#give us fields for Username, Password, and submition
from wtforms import StringField, BooleanField ,PasswordField, SubmitField
#check that user send a date
from wtforms.validators import DataRequired, Email, EqualTo

class Loginform(FlaskForm):
    username = StringField('User name', validators=[DataRequired()], render_kw={'class':"form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class':"form-control"})
    remember_me = BooleanField("Remember me", default=True ,render_kw={'class': 'form-check-input'})
    submit = SubmitField('Send', render_kw={'class':'btn btn-primary'})
    
class RegistrationForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired()], render_kw={'class':"form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'class':"form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class':"form-control"})
    password2 = PasswordField('Write Password again', validators=[DataRequired(), EqualTo('password')], render_kw={'class':"form-control"})
    submit = SubmitField('Send', render_kw={'class':'btn btn-primary'})