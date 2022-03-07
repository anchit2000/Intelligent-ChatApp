from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from utils.mysql_connection import cursor


class MyForm(FlaskForm):
    username = StringField('username', validators=[validators.data_required()])
    password = PasswordField('password', validators=[validators.data_required()])
    send = SubmitField('send')


def check_password(username, password):
    cursor.execute(f"select * from user_table where username = '{username}';")
    result = cursor.fetchall()
    print(result)
    if result:
        date_created = ""
        return 1
    else:
        return 2
