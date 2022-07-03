from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from user import UserRegister
from item import Item

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)


# -------------------------------------------------------

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

# -------------------------------------------------------




api.add_resource(UserRegister, "/signup")
api.add_resource(Item, "/item/<string:name>")

app.run(debug=True)