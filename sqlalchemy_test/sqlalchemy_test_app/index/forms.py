from flask_wtf import FlaskForm
from wtforms import Field, Form, IntegerField, StringField, SubmitField

class DataForm(FlaskForm):
    """
    Form for entering data to be stored in the database.
    """
    id = IntegerField("ID")
    name = StringField("Name")
    value = IntegerField("Value: This string comes from label attribute.")
    submit = SubmitField("Submit")

class ConfirmationForm(FlaskForm):
    """
    Confirmation
    """
    previous_page = SubmitField("Got to Previous Page")
    confirm = SubmitField("Submit Confirmation")