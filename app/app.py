from dotenv import load_dotenv
from flask import Flask
from flask_babel import Babel

from app.db.db import create_db_connection
from app.routes import about_bp , insert_user_bp, get_users_bp, delete_user_bp, update_user_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    babel = Babel(app)

    create_db_connection(app)
    app.register_blueprint(about_bp) 
    app.register_blueprint(insert_user_bp)
    app.register_blueprint(get_users_bp) 
    app.register_blueprint(delete_user_bp)
    app.register_blueprint(update_user_bp) 

    return app

app = create_app()

if __name__ == "__main__":
    app.run()
