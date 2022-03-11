from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators

from utils.get_user_data import UserData

class MyForm(FlaskForm):
    username = StringField('username', validators=[validators.data_required()])
    password = PasswordField('password', validators=[validators.data_required()])
    send = SubmitField('send')

class newAccountForm(MyForm):
    name = StringField('name', validators=[validators.data_required()])

# TODO : PASSWORD SHOULD BE ENCRYPTED WITH DATE FOR STORING IN DB
def check_password(username, password):
    result = UserData(username).get_user_details()
    if result:
        # id = result['id']
        # name = result['name']
        # username = result['username']
        # profile_picture = result['profile_picture']
        # date_created = result['date_created']
        password_ = result['password_']
        if password == password_:
            return 1
        else:
            return 3
    else:
        return 2
