from flask import Blueprint, render_template

users = Blueprint('users', __name__,
                         static_folder='static',
                         template_folder='templates')

@users.route('/users')
def users_func():
    return render_template('users.html')