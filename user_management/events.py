class UserCreated:
    def __init__(self, username, score=0):
        self.username = username
        self.score = score

    def as_dict(self):
        return {"username": self.username, "score": self.score}


class UserUpdated(UserCreated):
    pass


class UserDeleted:
    def __init__(self, delete_key):
        self.delete_key = delete_key
