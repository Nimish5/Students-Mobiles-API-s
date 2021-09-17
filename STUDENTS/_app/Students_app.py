from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Verification import authenticate, identity
from resources.User import User_Register
from resources.Students_info import Students, All_Students

app = Flask(__name__)
app.secret_key = "ShubhamJain25"
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/CrossCheck'

jwt = JWT(app, authenticate, identity)      # (/auth - By deafult)

api.add_resource(User_Register, '/SignUp')
api.add_resource(Students, '/student/<string:name>')
api.add_resource(All_Students, '/Students')

if __name__ == "__main__":
    app.run(debug=True)
