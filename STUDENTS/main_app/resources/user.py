from flask_restful import Resource, reqparse
from models.user import UserModel

class User_SignUp(Resource):
    shubham = reqparse.RequestParser()
    shubham.add_argument("Username", type=str, required=True, help="Mandatory Field")
    shubham.add_argument('Password', type=str, required=True, help='Mandatory Field')

    def post(self):
        payload = User_SignUp.shubham.parse_args()

        if UserModel.find_by_username(payload['Username']):
            return f"The Username '{payload['Username']} 'already exist in the Users database!"

        New_User = UserModel(payload['Username'], payload['Password'])
        New_User.Save_Credentials_to_db()

        return {'Messege': 'The User is Created/ Registered Sucessfully!'}


