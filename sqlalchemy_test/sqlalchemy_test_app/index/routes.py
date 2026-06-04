from flask import current_app, render_template, request, redirect, url_for
from flask import session as web_session
from ..index import bp


from .forms import DataForm, ConfirmationForm
from ..models import Score
from ..extensions import db


def __print_info():
    print(f"request: {request}")
    print(f"request form: {request.form}")

@bp.route("/", methods=["GET", "POST"])
def index():
    """
    Render the Default Usint page
    """

    #: Request form is the form data which exists during a web request. This isn't a store of your intended input of the user data,
    #: This is only a state of the HTTP request, which is built to be stateless
    #: In flask application, we combine these two sources of data into a populated form of user input.
    form = DataForm(request.form, data = web_session)

    __print_info()

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        value = form.value.data
        web_session['id'] = id
        web_session['name'] = name
        web_session['value'] = value
        #: url_for() dynamically maps internal name of a view function endpoint to it's corresponding URL path.
        #: all the @app.route or @bp.route function decorators register the view function endpoints
        #: For functionally running python code, and then rendering HTML pages.
        return redirect(url_for("index.confirmation"))

    return render_template("index.jinja", form=form)

bp.route("/confirmation", methods=["GET", "POST"])
def confirmation():
    """
    Use web_session to display a confirmation page of the intermediary data.

    If successfully confirmed, this then writes to the database.
    The page redirection order specifically so that transactions are not repeated by a user refreshing the page.
    https://en.wikipedia.org/wiki/Post/Redirect/Get
    """

    form = ConfirmationForm(request.form)

    __print_info()

    if form.validate_on_submit():
        if form.previous_page.data:
            redirect(url_for("index.index"))
        
        if form.confirm.data:
            #: The confirm button was pushed! perform the database operation
            new_entry= Score(
                            id=web_session.id,
                            name=web_session.name,
                            value=web_session.value
                        )
            
            db.session.add(new_entry)
            db.session.commit()
            redirect(url_for("index.submitted"))
    
    return render_template("confirmation.jinja", form=form)

@bp.route("/submitted", methods=["GET"])
def submitted():
    """
    Render the Submission Confirmation page
    """
    id = web_session.pop('id')
    name= web_session.pop('name')
    value = web_session.pop('value')
    return render_template("submitted.jinja", id = id, name=name, value=value)