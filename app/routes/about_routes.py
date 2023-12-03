from flask import Blueprint

about_bp = Blueprint('about', __name__)

@about_bp.route('/api/about')
def about():
    return 'CRUD em Flask, ok! 🐍'
