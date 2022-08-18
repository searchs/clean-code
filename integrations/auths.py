class Authentication:
    USERS = [
        { "username": "user1", "password": "pwd1" },
        { "username": "user2", "password": "pwd2" },
        ]

    def login(self, username, password):
        u = self.fetch_user(username)
        if not u or u["password"] != password:
            return None
        return u

    def fetch_user(self, username):
        for u in self.USERS:
            if u["username"] == username:
                return u
            return None



class Authorization:
    PERMISSIONS = [
        {"user": "user1",
         "permissions": {
             "view","create", "edit", "delete"
         }}
    ]
    def can(self, user, action):
        for u in self.PERMISSIONS:
            if u["user"] == user["username"]:
                return action in u["permissions"] #returns Truein action in user permissions
            return False

