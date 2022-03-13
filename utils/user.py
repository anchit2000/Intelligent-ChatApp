class User:

    def __init__(self, id, username, password):
        self.username = username
        self.password = password
        self.id = id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username
