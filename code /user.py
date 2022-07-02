import  sqlite3




class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id
    
    @classmethod
    def find_by_username(cls, username):

        db = sqlite3.Connection("data.db")
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username, ))
        row = result.fetchone()
        if row :
            user = cls(*row)
        else:
            user = None
        return user


    @classmethod
    def find_by_id(cls, _id):

        db = sqlite3.Connection("data.db")
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (id, ))
        row = result.fetchone()
        if row :
            user = cls(*row)
        else:
            user = None
        return user