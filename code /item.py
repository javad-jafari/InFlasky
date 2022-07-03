import  sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required




class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("price",
    type=int,
    required=True,
    help="this is required !"    
    )

    @classmethod
    def find_by_name(cls, name):

        db = sqlite3.Connection("data.db")
        cursor = db.cursor()

        query= "select * from items where name=?"

        res = cursor.execute(query, (name, ))

        row = res.fetchone()
        db.close()

        if row:
            return {"item" : {"name":row[1],  "price":row[2]}}


    def get(self, name):

        item = self.find_by_name(name)
        if item:
            return item, 200
        return {"message" : "item is not exist"}, 404

    def post(self, name):

        if self.find_by_name(name):
            return {"message" : "item is alread exist"}

        data = Item.parser.parse_args()

        db = sqlite3.Connection("data.db")
        cursor = db.cursor()

        query= "insert into items values (NULL, ?, ?)"
        
        cursor.execute(query, (name, data["price"]))
        db.commit()
        db.close()
        return {"message": f"item {name} , price : {data['price']} create"}, 201

