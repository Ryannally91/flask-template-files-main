from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
# from flask_app.models.user import User

# CREATE controller
@app.route("/users/create", methods = ['POST'])
def create_user():
    print('^^^^^^^^^^^^^^^^^', request.form)
    user.User.create_user(request.form)
    return redirect('/')


# READ controller

@app.route('/')
def index():
    all_users = user.User.get_all_users()
    return render_template('index.html', users = all_users)


# UPDATE controller

@app.route('/users/update/<id>')
def update_form(id):
    this_user = user.User.get_user_by_id(id)
    return render_template('update_user.html', user = this_user)

@app.route('/users/update/process', methods = ['POST'])
def process_update():
    user.User.update_user(request.form)
    return redirect('/')


# DELETE controller

@app.route('/users/delete/<id>')
def delete_user(id):
    user.User.delete_user(id)
    return redirect('/')

@app.route('/users/profile/<id>')
def profile(id):
    user.User.get_user_by_id(id)