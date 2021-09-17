from flask_restful import Resource, reqparse
from models.user import UserModel
        
class User_SignUp(Resource):      # To Register to new users in the database
    parser = reqparse.RequestParser()
    parser.add_argument("Username", type=str, required=True, help="Mandatory Field!")
    parser.add_argument("Password", type=str, required=True, help="Manadtory Field!")

    def post(self):
        payload = User_SignUp.parser.parse_args()

        if UserModel.find_by_username(payload['Username']):
            return f"A user with the name '{payload['Username']}' already exists in the Users database!", 400

        user = UserModel(payload['Username'], payload['Password'])     # user = UserModel(**payload) 
        user.save_to_db()

        return {'Message': 'User created/ Register sucessfully!'}

