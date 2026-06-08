from flask import Blueprint, request
bp = Blueprint('pathing', __name__)

import logging

@bp.route('/')
def show_address():
    full_url = request.url
    base_url = request.base_url
    host_url = request.host_url
    client_ip = request.remote_addr

    return f"""
    Full URL: {full_url} <br>
    Base URL: {base_url} <br>
    Host URL: {host_url} <br>
    Your IP: {client_ip}
    """

@bp.route('logging')
def show_logging():
    gunicorn = logging.getLogger("gunicorn")
    gunicorn_error = logging.getLogger("gunicorn.error")
    gunicorn_access = logging.getLogger("gunicorn.access")

    gunicorn_access.info("Test Line for access")

    return f"""
    gunicorn: {gunicorn.__dict__} <br>
    gunicorn_error: {gunicorn_error.__dict__} <br>
    gunicorn_access: {gunicorn_access.__dict__} <br>
    """