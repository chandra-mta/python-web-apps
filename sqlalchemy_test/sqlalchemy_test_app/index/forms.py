from flask_wtf import FlaskForm
from wtforms import Field, Form, IntegerField, StringField, SubmitField

class DataForm(FlaskForm):
    """
    Form for entering data to be stored in the database.
    """
    name = StringField("Name")
    value = IntegerField("Value")
    submit = SubmitField("Submit")