import os
import psycopg2
from flask import Flask

def create_db_connection(app: Flask):
    db_url = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(db_url)
    app.db_connection = connection
    return connection
