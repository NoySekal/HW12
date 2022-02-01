from flask import Blueprint, render_template, request, redirect
from interact_db import interact_db

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path="/assignment10.html", template_folder='templates')


@assignment10.route('/assignment10')
def assignment10_func():
    return render_template('assignment10.html')


@assignment10.route('/creat_new_user', methods=['POST'])
def creat_new_user_func():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query = "INSERT INTO users (name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
    interact_db(query=query, query_type='commit')
    return redirect('/user_list')


@assignment10.route('/update_user_password', methods=['POST'])
def update_user_password_func():
    user_id = request.form['user_id']
    password = request.form['last_password']
    new_password = request.form['new_password']
    query = "update users set password = '%s' where id = '%s' and password = '%s';" % (new_password, user_id, password)
    interact_db(query=query, query_type='commit')
    return redirect('/user_list')


@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user_id']
    password = request.form['password']
    query = "DELETE FROM users where id = '%s' and password = '%s';" % (user_id, password)
    interact_db(query=query, query_type='commit')
    return redirect('/user_list')


@assignment10.route('/user_list')
def print_users_func():  # put application's code here
    query = 'select * from users'
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', user_list=query_result)