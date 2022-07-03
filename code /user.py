import  sqlite3
from flask_restful import Resource, reqparse




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
        result = cursor.execute(query, (_id, ))
        row = result.fetchone()
        if row :
            user = cls(*row)
        else:
            user = None
        return user




class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="this field can not be blank"
    )

    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="this field can not be blank"
    )


    def post(self):

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data["username"]):
            return {"message":"user already exist!"}, 400

        db = sqlite3.Connection("data.db")
        cursor = db.cursor()

        query = "INSERT INTO users values (NULL,?,?)"

        cursor.execute(query, (data["username"], data["password"]))

        db.commit()
        db.close()

        return {"message":"user registered successfully"}, 201 