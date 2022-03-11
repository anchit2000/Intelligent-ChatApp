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
                'id' : id,
                'name' : name,
                'username' : username,
                'profile_picture' : profile_picture,
                'date_created' : date_created,
                'password_' : password_
            }
        else:
            return {}

class CreateNew:
    def __init__(self,name,username,password,profile_picture = None):
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