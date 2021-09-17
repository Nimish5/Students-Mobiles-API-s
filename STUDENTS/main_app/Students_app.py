from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Verification import authenticate, identity
from resources.user import User_SignUp
from resources.Students_info import StudentClass, All_Students
from resources.Student_stores import Stores, Stores_List

app = Flask(__name__)
app.secret_key = 'Shubham26Jain'
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_database():
    db.create_all()

app.config['JWT_AUTH_URL_RULE'] = '/CrossCheck'

jwt = JWT(app, authenticate, identity)     # /auth(by Default)


api.add_resource(User_SignUp, '/SignUp')
api.add_resource(StudentClass, '/student/<string:name>')
api.add_resource(All_Students, '/Students')
api.add_resource(Stores, '/store/<string:name>')
api.add_resource(Stores_List, '/All_Stores')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)


    