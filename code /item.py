import  sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity




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

    @jwt_required()
    def get(self, name):

        item = self.find_by_name(name)
        if item:
            return item, 200
        return {"message" : "item is not exist"}, 404

    @classmethod
    def insert_item(cls, name):
        data = Item.parser.parse_args()

        db = sqlite3.Connection("data.db")
        cursor = db.cursor()

        query= "insert into items values (NULL, ?, ?)"
        
        cursor.execute(query, (name, data["price"]))
        db.commit()
        db.close()


    def post(self, name):

        if self.find_by_name(name):
            return {"message" : "item is alread exist"},409

        try:
            self.insert_item(name)
        except:

            return {"message": "An error occured in inserting item"},500

        return {"message": f"item {name}  create"}, 201


    def delete(self, name):

        if self.find_by_name(name) is None:
            return {"message" : "item is not exist to delete"}


        db = sqlite3.Connection("data.db")
        cursor = db.cursor()

        query= "delete from items where name=?"
        
        cursor.execute(query, (name, ))
        db.commit()
        db.close()
    
    def put(self, name):

        data = Item.parser.parse_args()
        update_item = {"name":name, "price":data["price"]}
        if self.find_by_name(name):
        
            try:
                self.update_item(**update_item)

            except:
                return {"message":"An error occured in updating item"}        
        
        
        try:
            self.insert_item(name)
        except:
            return {"message":"An error occured in inserting item?"}




        return update_item, 200


    @classmethod
    def update_item(cls, name, price):

        db = sqlite3.Connection("data.db")
        cursor = db.cursor()

        query= "update items set price=? where name=?"
        
        cursor.execute(query, (price, name))
        db.commit()
        db.close()
    