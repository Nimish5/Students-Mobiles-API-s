# Section6 - Video 93: Creating User & Item models

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.Mobiles_data import PhoneModel
import sqlite3

class Phone(Resource):
    nimish = reqparse.RequestParser()
    nimish.add_argument('Mobile', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Company', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Price', type=int, required=True, help='This field is mandatory!')
    nimish.add_argument('IMEI_No', type=str, required=True, help='This field is mandatory!')
    
    @jwt_required()
    def get(self, name):
        item = PhoneModel.name_existance(name)         # self.name_existance(name)
        if item:
            return item.json()
        return f"The {name} is not in the Mobiles database!", 404

    def post(self, name):
        if PhoneModel.name_existance(name):
            return {'Message': f'The item with {name} is already exists in the Mobiles database!'}

        input = Phone.nimish.parse_args()

        item = PhoneModel(name, input['Mobile'], input['Company'], input['Price'], input['IMEI_No'])

        try:
            item.storing()             
        except:
            {'Message': 'An error occured in storing an item.'}, 500
        
        return item.json(), 201

    def put(self, name):
        data = Phone.nimish.parse_args()

        item = PhoneModel.name_existance(name)
        Mobile = PhoneModel(name, data['Mobile'], data['Company'], data['Price'], data['IMEI_No'])

        if item:
            Mobile.modify()
        else:
            Mobile.storing()

        return Mobile.json(), 201

    def delete(self, name):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "DELETE FROM Mobiles WHERE Name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'Message': f'An item {name} is deleted from the Mobiles database!'}


class Phone_List(Resource):
    def get(self):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Mobiles"
        result = cursor.execute(query)

        Mobiles = []
        for data in result:          # for row in result
            Mobiles.append({'Name': data[0], 'Mobile': data[1], 'Company': data[2], 'Price': data[3],
            'IMEI_No': data[4]})

        connection.close()

        return {'Mobiles': Mobiles}


