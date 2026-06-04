from flask import Flask
from .config import BaseConfig

from .extensions import db, web_session_instance, bootstrap

from werkzeug.middleware.proxy_fix import ProxyFix

#
# --- SQLAlchemy event handler to turn on Foreign Key Constraints for every engine connection.
#
from sqlalchemy.engine import Engine
from sqlalchemy import event


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    bootstrap.init_app(app)
    db.init_app(app)
    app.config['SESSION_SQLALCHEMY'] = db #: Must set the SQLAlchemy database for server-side session data after construction
    web_session_instance.init_app(app)

    #: Binds application instance to current CPU thread for using current_app and g proxies.
    # app.app_context().push()


    #: Register Routes
    from .index import bp as index_bp

    app.register_blueprint(index_bp, url_prefix="/")

    app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)

    return app