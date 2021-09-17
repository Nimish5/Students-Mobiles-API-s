# Section6 : Simplifying storage with FLASK-SQLAlchemy
# Video 93: Creating User & Item models

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Authentication import authenticate, identity
from resources.user import User_SignUp
from resources.Mobiles_data import Phone, Phone_List

app = Flask(__name__)
app.secret_key = "Nimish05"
api = Api(app)

# To change the URL of the authetication end point(/auth - by default)
app.config['JWT_AUTH_URL_RULE'] = '/Login'

jwt = JWT(app, authenticate, identity)   

# To change the JWT-Token expiration time i.e 5min(Default)
# app.config['JWT_EXPIRATION_DELTA'] = 'timedelta(seconds=1800)'       #  token will expire in 10 mins
 

api.add_resource(Phone, "/mobile/<string:name>")
api.add_resource(Phone_List, "/Mobiles")
api.add_resource(User_SignUp, "/Register")

if __name__ == "__main__":
    app.run(debug=True)