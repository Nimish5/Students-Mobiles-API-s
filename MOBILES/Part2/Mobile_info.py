# Section6 : Simplifying storage with FLASK-SQLAlchemy
# Video 95 - 99: 

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Authentication import authenticate, identity
from resources.user import User_SignUp
from resources.Mobiles_data import Phone, Phone_List
from resources.Mobile_stores import Store, Stores_list

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqldata.db'           # Video 101: No More Creating Tables
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False         #  Video 97: Explanation(8:45 - 10:20)
app.secret_key = "Nimish05"
api = Api(app)

@app.before_first_request             # Section 6: Video 101 - No more creating tables manually
def create_tables():
    db.create_all()

# To change the URL of the authetication end point(/auth - by default)
app.config['JWT_AUTH_URL_RULE'] = '/Login'

jwt = JWT(app, authenticate, identity)      # /auth(by default)

# To change the JWT-Token expiration time i.e 5min(Default)
# app.config['JWT_EXPIRATION_DELTA'] = 'timedelta(seconds=1800)'       #  token will expire in 10 mins
 

api.add_resource(Phone, "/mobile/<string:name>")
api.add_resource(Phone_List, "/Mobiles")
api.add_resource(User_SignUp, "/Register")
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores_list, '/Stores')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)


