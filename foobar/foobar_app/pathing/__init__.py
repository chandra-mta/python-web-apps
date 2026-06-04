from flask import Blueprint, request
bp = Blueprint('pathing', __name__)

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