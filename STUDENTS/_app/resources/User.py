from flask_restful import Resource, reqparse
from models.User import UserModel
import sqlite3

class User_Register(Resource):
    suds_neha = reqparse.RequestParser()
    suds_neha.add_argument('Username', type=str, required=True, help='This field is mandatory!')
    suds_neha.add_argument('Password', type=str, required=True, help='This field is mandatory!')

    def post(self):
        payload = User_Register.suds_neha.parse_args()

        if UserModel.Search_By_Username(payload['Username']):
            return {'Messege': f"The user '{payload['Username']}' already exist in Users Database/ Table"}

        connection = sqlite3.connect('Mydatabasefile.db')
        cursor = connection.cursor()

        query = 'INSERT INTO Users VALUES (NULL, ?, ?)'
        cursor.execute(query, (payload['Username'], payload['Password']))

        connection.commit()
        connection.close()

        return {'Messege': 'User Registration Sucessfully!'}