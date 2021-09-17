from flask_restful import Resource, reqparse
from models.user import UserModel
import sqlite3
        
class User_SignUp(Resource):      # To Register to new users in the database
    parser = reqparse.RequestParser()
    parser.add_argument("Username", type=str, required=True, help="Mandatory Field!")
    parser.add_argument("Password", type=str, required=True, help="Manadtory Field!")

    def post(self):
        payload = User_SignUp.parser.parse_args()

        if UserModel.find_by_username(payload['Username']):
            return f"A user with the name '{payload['Username']}' already exists in the Users database!", 400
        
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()
 
        query = "INSERT INTO Users VALUES (NULL, ?, ?)"
        cursor.execute(query, (payload['Username'], payload['Password']))

        connection.commit()
        connection.close()

        return {'Message': 'User created/ Register sucessfully!'}

