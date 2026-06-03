from flask import Blueprint, render_template
bp = Blueprint('index', __name__)
from .. import config

@bp.route("/", methods=["GET", "POST"])
def index():
    """
    Render the Default Usint page
    """

    return render_template("index.jinja", external_thing=config.external_thing)