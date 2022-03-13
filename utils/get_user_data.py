from utils.mysql_connection import cursor, conn

from datetime import datetime


class UserData:
    def __init__(self, username):
        self.username = username

    def get_user_details(self):
        cursor.execute(f"select * from user_table where username = '{self.username}';")
        result = cursor.fetchall()
        if result:
            id, name, username, profile_picture, date_created, password_ = result[0]
            return {
                'id': id,
                'name': name,
                'username': username,
                'profile_picture': profile_picture,
                'date_created': date_created,
                'password_': password_
            }
        else:
            return {}

    def find_user_friends(self):
        cursor.execute(f"select id from user_table where username = '{self.username}';")
        id_username = cursor.fetchall()[0][0]
        cursor.execute(
            f"select from_, to_ from conversation_table where from_ = '{id_username}' or to_ = '{id_username}';")
        result = cursor.fetchall()
        ids = [i[0] for i in result if i[0] != id_username] + [i[1] for i in result if i[1] != id_username]
        if ids:
            cursor.execute(f"select id, name_, username from user_table where id in {tuple(ids)};")
            result = cursor.fetchall()
            ids = [i[0] for i in result if i[0] != id_username]
            names = [i[1] for i in result if i[0] != id_username]
            usernames = [i[2] for i in result if i[0] != id_username]
        else:
            ids, names, usernames = [], [], []
        return {
            'ids': ids,
            'names': names,
            'usernames': usernames
        }

    def get_all_users(self):
        cursor.execute(f"SELECT id, name_, username FROM user_table where username != '{self.username}';")
        result = cursor.fetchall()
        if result:
            ids = [i[0] for i in result]
            names = [i[1] for i in result]
            usernames = [i[2] for i in result]
        else:
            ids, names, usernames = [], [], []
        return {
            'ids': ids,
            'names': names,
            'usernames': usernames
        }



class CreateNew:
    def __init__(self, name, username, password, profile_picture=None):
        self.time_now = datetime.utcnow()
        self.name = name
        self.username = username
        self.password = password
        self.profile_picture = profile_picture

    def create_user(self):
        try:
            cursor.execute(
                '''
                INSERT INTO user_table (name_,username,password_,date_created)
                VALUES (%s,%s,%s,%s)
                ''',
                (self.name,
                 self.username,
                 self.password,
                 self.time_now)
            )
            conn.commit()
            return 1
        except Exception as e:
            print(e)
            return 2
