from flask_wtf import FlaskForm # we need it for creating a form
#give us fields for Username, Password, and submition
from wtforms import StringField, BooleanField ,PasswordField, SubmitField
#check that user send a date
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
    username = StringField('User name', validators=[DataRequired()], render_kw={'class':"form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class':"form-control"})
    remember_me = BooleanField("Remember me", default=True ,render_kw={'class': 'form-check-input'})
    submit = SubmitField('Send', render_kw={'class':'btn btn-primary'})