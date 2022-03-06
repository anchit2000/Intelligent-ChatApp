from flask import Flask, Blueprint, redirect

app = Flask(__name__)


# app.register_blueprint()

@app.route("/")
def check_user():
    return redirect("/login")


@app.route("/login")
def login_signup():
    return "signin"


@app.route("/test_service")
def test_if_live():
    return "The service is running"


if __name__ == '__main__':
    app.run()
