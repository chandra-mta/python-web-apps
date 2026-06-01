from flask import current_app, render_template, request, flash, session, redirect, url_for
from ..index import bp
from .forms import DataForm

@bp.route("/", methods=["GET", "POST"])
def index():
    """
    Render the Default Usint page
    """

    form = DataForm(request.form, data = session)
    if form.validate_on_submit():
        name = form.name.data
        value = form.value.data
        session["name"] = name
        session["value"] = value
        return redirect(url_for("index.submitted"))

    return render_template("index.jinja", form=form)

@bp.route("/submitted", methods=["GET"])
def submitted():
    """
    Render the Submission Confirmation page
    """
    return render_template("submitted.jinja", name=session.get("name"), value=session.get("value"))