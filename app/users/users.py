import uuid
class User(object):
    def __init__(self, name, email, userName, password, id = None):
        self.name = name
        self.email = email
        self.userName = userName
        self.password = password
        self.id = uuid.uuid4().hex if id is None else id  