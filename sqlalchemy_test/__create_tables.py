#! /usr/bin/env python
"""
This script creates the tables in the database for the SQLAlchemy test app if not yet created.
Necessary to prevent multiple server process workers from trying to create tables simultaneously. No worker should be creating a table at runtime.
"""
from sqlalchemy_test_app import create_app, db

app = create_app()
with app.app_context():
    db.create_all()