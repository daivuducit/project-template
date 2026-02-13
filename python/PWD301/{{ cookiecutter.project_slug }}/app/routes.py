from flask import Blueprint, render_template, jsonify
from app.models import User

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html', title='Home')

@bp.route('/about')
def about():
    return render_template('about.html', title='About')

@bp.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

# API Endpoints
@bp.route('/api/users')
def api_users():
    users = User.get_all()
    return jsonify({'success': True, 'users': users})

@bp.route('/api/user/<int:user_id>')
def api_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        return jsonify({'success': True, 'user': user})
    return jsonify({'success': False, 'error': 'User not found'}), 404