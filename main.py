import flask
from flask import Flask, redirect, request, render_template, jsonify, flash, url_for
from utils.form_validation import MyForm, check_password, newAccountForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from utils.user import User
from utils.get_user_data import UserData, CreateNew
import os
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

socketio = SocketIO(app)


@login_manager.user_loader
def load_user(username):
    result = UserData(username).get_user_details()
    return User(username=username, password=result['password_'], id=result['id'])


# app.register_blueprint()
@app.route("/")
def check_user():
    # check if user is logged in
    if current_user.is_authenticated:
        return redirect("/home")
    else:
        return redirect("/login")


@app.route("/login", methods=['GET', 'POST'])
def login_signup():
    if current_user.is_authenticated:
        return redirect("/home")
    else:
        form = MyForm()
        return render_template("login_signup.html", form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_signup'))


@app.route("/create", methods=['GET', 'POST'])
def create_new_account():
    form = newAccountForm()
    if form.validate_on_submit():
        if request.method == "POST":
            name = request.form['name']
            username = request.form['username']
            password = request.form['password']
            res = check_password(username, password)
            if res['result'] == 2:
                resp = CreateNew(name, username, password).create_user()
                if resp == 1:
                    login_user(user=User(username, password), remember=True)
                    return redirect(url_for('home'))
                elif resp == 2:
                    flask.flash("USERNAME ALREADY TAKEN!")
                    return redirect(url_for('create_account'))
            else:
                return redirect("/login")
        else:
            return jsonify(request.method)
    else:
        try:
            return jsonify(form.errors)
        except Exception as e:
            return str(jsonify(e)) + str(form.errors)


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    form = MyForm()
    # print(form.validate_on_submit())
    # print(request.form)
    if form.validate_on_submit():
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            res = check_password(username, password)
            if res['result'] == 1:
                user_ = User(username=username, password=password,id=res['user_details']['id'])
                login_user(user=user_, remember=True)
                return redirect('/home')
            elif res['result'] == 2:
                return render_template("new account.html")
            else:
                flash("Wrong password")
                return redirect('/login')
        else:
            return jsonify("Something went down")
    else:
        try:
            return jsonify(form.errors)
        except Exception as e:
            return str(jsonify(e)) + str(form.errors)


@app.route("/create_account")
def create_account():
    form = newAccountForm()
    return render_template("new account form.html", form=form)


@app.route("/home")
@login_required
def home():
    if current_user.is_authenticated:
        return f"Welcome back, {current_user.username}, your id is {current_user.id}"
    else:
        return redirect(url_for('login_signup'))


@app.route("/test_service")
def test_if_live():
    return "The service is running"


if __name__ == '__main__':
    socketio.run(debug=True)
