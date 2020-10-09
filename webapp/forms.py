from flask_wtf import FlaskForm # we need it for creating a form
#give us fields for Username, Password, and submition
from wtforms import StringField,  PasswordField, SubmitField
#check that user send a date
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
    username = StringField('User name', validators=[DataRequired()], render_kw={'class':"form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class':"form-control"})
    submit = SubmitField('Send', render_kw={'class':'btn btn-primary'})