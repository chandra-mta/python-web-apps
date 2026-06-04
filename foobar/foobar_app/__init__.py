from flask import Flask
from .config import BaseConfig
from flask_bootstrap import Bootstrap5


bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    bootstrap.init_app(app)

    #: Register Routes
    from .index import bp as index_bp

    app.register_blueprint(index_bp, url_prefix="/")

    from .pathing import bp as pathing_bp

    app.register_blueprint(pathing_bp, url_prefix="/pathing")

    return app
