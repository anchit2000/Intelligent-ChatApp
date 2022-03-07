from flask import Flask, redirect, request, render_template, jsonify
from utils.mysql_connection import cursor
from utils.form_validation import MyForm, check_password
from flask_login import LoginManager
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# app.register_blueprint()

@app.route("/")
def check_user():
    # check if user is logged in
    return redirect("/login")


@app.route("/login", methods=['GET', 'POST'])
def login_signup():
    form = MyForm()
    return render_template("login_signup.html", form=form)


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    form = MyForm()
    print(form.validate_on_submit())
    print(request.form)
    if form.validate_on_submit():
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            if check_password(username, password) == 1:
                return jsonify(username if username else "nothing")
            elif check_password(username,password) == 2:
                return render_template("new account.html")
        else:
            return redirect('/home')
    else:
        try:
            return jsonify(form.errors)
        except Exception as e:
            return str(jsonify(e)) + str(form.errors)

@app.route("/create_account")
def create_account():
    return "create account"


@app.route("/home")
def home():
    return "home"


@app.route("/test_service")
def test_if_live():
    return "The service is running"


if __name__ == '__main__':
    app.run(debug=True)
