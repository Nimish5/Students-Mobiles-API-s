# Section 6: Video 103(Creating the Store Resource)

from flask_restful import Resource
from models.Student_stores import StoreModel

class Stores(Resource):
    def get(self, name):
        store = StoreModel.find_by_StoreName(name)
        if store:
            return store.json(), 200
        return {'Messege': f'The store dose not exist with the name {name} in Students database!'}, 404

    def post(self, name):
        if StoreModel.find_by_StoreName(name):
            return 'A store with the name {} already exist in the Stores database!'.format(name), 400  

        store = StoreModel(name)
        
        try:
            store.Save_to_db()
        except:
            {'Messege': 'An error occured while saving/ storing a store.'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_StoreName(name)
        if store:
            store.Delete_from_db()
        
        return {'Messege': f'The store {name} is deleted Sucessfully!'}


class Stores_List(Resource):
    def get(self):
        return {'Stores': [store.json() for store in StoreModel.query.all()]}


