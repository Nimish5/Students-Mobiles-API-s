# Video 103: Creating the Store Resource

from flask_restful import Resource
from models.Mobile_stores import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.name_existance(name)
        if store:
            return store.json()
        return {'Message': "There is no store with the name {} in the Stores database!".format(name)}, 404

    def post(self, name):
        if StoreModel.name_existance(name):
            return {f'A store with the name {name} already exist in the Stores database!'}, 400

        store = StoreModel(name)
        try:
            store.storing_modify()
        except:
            return {'Messege': 'An error occured while creating an store'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.name_existance(name)
        if store:
            store.delete_from_db()
        return {'Message': f'The Store {name} is deleted Sucessfully!'}


class Stores_list(Resource):
    def get(self):
        return {'Stores': [store.json() for store in StoreModel.query.all()]}