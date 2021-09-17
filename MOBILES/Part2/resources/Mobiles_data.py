# Video 95 - 99: Creating User & Item models

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.Mobiles_data import PhoneModel

class Phone(Resource):
    nimish = reqparse.RequestParser()
    nimish.add_argument('Mobile', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Company', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Price', type=int, required=True, help='This field is mandatory!')
    nimish.add_argument('IMEI_No', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Store_id', type=int, required=True, help='Every Mobile needs an store id!')
    
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

        Mobile = PhoneModel(name, input['Mobile'], input['Company'], input['Price'], input['IMEI_No'], input['Store_id'])   

        try:
            Mobile.storing_modify()             
        except:
            {'Message': 'An error occured in storing an item.'}, 500
        
        return Mobile.json(), 201

    def put(self, name):
        data = Phone.nimish.parse_args()

        item = PhoneModel.name_existance(name)
        # Mobile = PhoneModel(name, data['Mobile'], data['Company'], data['Price'], data['IMEI_No'])

        if item is None:
            item = PhoneModel(name, data['Mobile'], data['Company'], data['Price'], data['IMEI_No'], data['Store_id'])  
        else:
            item.Mobile, item.Company, item.Price, item.IMEI_No, item.store_id = data['Mobile'], data['Company'], data['Price'], data['IMEI_No'], data['Store_id']  

        item.storing_modify() 

        return item.json(), 201

    def delete(self, name):
        item = PhoneModel.name_existance(name)
        if item:
            item.delete_from_db()

        return {'Message': f'An item {name} is deleted from the Mobiles database!'}


class Phone_List(Resource):
    def get(self):
        return {'Mobiles': [Mobile.json() for Mobile in PhoneModel.query.all()]}
        # {'Mobiles': list(map(lambda x: x.json(), PhoneModel.query.all()))}




