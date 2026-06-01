#from flask import current_app, render_template, request, flash, session, redirect, url_for
from ..index import bp

@bp.route("/", methods=["GET", "POST"])
def index():
    """
    Render the Default Usint page
    """
    #return render_template("index.html")
    return "<p> Hello World! </p>"