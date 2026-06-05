import os
import logging
from logging.handlers import RotatingFileHandler


def build_rotating_handler(path, level):
    handler = RotatingFileHandler(
        path,
        maxBytes=1 * 1024, # 2kb
        backupCount=7
    )

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    )
    handler.setFormatter(formatter)
    handler.setLevel(level)

    return handler


def configure_all_logging(app_root):
    log_dir = os.path.join(app_root, "instance", "logs")
    os.makedirs(log_dir, exist_ok=True)

    # ----------------------------------------------------------------------
    # Gunicorn error logger
    # ----------------------------------------------------------------------
    gunicorn_error = logging.getLogger("gunicorn.error")
    gunicorn_error.handlers.clear()
    gunicorn_error.addHandler(
        build_rotating_handler(
            os.path.join(log_dir, "gunicorn_error.log"),
            logging.INFO
        )
    )
    gunicorn_error.setLevel(logging.INFO)

    # ----------------------------------------------------------------------
    # Gunicorn access logger
    # ----------------------------------------------------------------------
    gunicorn_access = logging.getLogger("gunicorn.access")
    gunicorn_access.handlers.clear()
    gunicorn_access.addHandler(
        build_rotating_handler(
            os.path.join(log_dir, "gunicorn_access.log"),
            logging.INFO
        )
    )
    gunicorn_access.setLevel(logging.INFO)