from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.Students_info import StudentModel
import sqlite3

class Students(Resource):

    Shubham = reqparse.RequestParser()
    Shubham.add_argument('FamilyName', type=str, required=True, help='This field is Mandatory!')
    Shubham.add_argument('Age', type=int, required=True, help='This field is Mandatory!')
    Shubham.add_argument('CollegeName', type=str, required=True, help='This field is Mandatory!')
    Shubham.add_argument('Student_id', type=str, required=True, help='This field is Mandatory!')
    Shubham.add_argument('Stream', type=str, required=True, help='This field is Mandatory!')
    Shubham.add_argument('ClassSection', type=str, required=True, help='This field is Mandatory!')

    @jwt_required()
    def get(self, name):
        item = StudentModel.Search_By_Name(name)
        if item:
            return item.json(), 200
        else:
            return {'Messege': f"The Student '{name}' dosen't exist in the Students Database!"}

    def post(self, name):
        if StudentModel.Search_By_Name(name):
            return f'The Student {name} already exist in the Students Database!'

        payload = Students.Shubham.parse_args()

        student = StudentModel(name, payload['FamilyName'], payload['Age'], payload['CollegeName'],
        payload['Student_id'], payload['Stream'], payload['ClassSection'])

        # try:
        student.Save_to_Database()
        # except:
        #     return {'Messege': 'An error occured in saving the Student in the Students Database!'}, 500
        
        return student.json(), 201

    def put(self, name):
        payload = Students.Shubham.parse_args()

        item = StudentModel.Search_By_Name(name)

        student = StudentModel(name, payload['FamilyName'], payload['Age'], payload['CollegeName'], 
        payload['Student_id'], payload['Stream'], payload['ClassSection'])

        if item:
            try:
                student.Updation()
            except:
                return f"An error occured in upadting the Students database!", 500
        else:
            try:
                student.Save_to_Database()
            except:
                return {'Messege': f'An error occured in inserting a student into Students table'}, 500

        return student.json(), 201

    def delete(self, name):
        student = StudentModel.Search_By_Name(name)

        if student:
            student.Delete_from_Database()
        return {'Messege': f"The Student '{name}' is deleted from the Students Database!"}


class All_Students(Resource):
    def get(self):
        connection = sqlite3.connect('Mydatabasefile.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM Students'
        result = cursor.execute(query)

        Students = []
        for student in result:
            Students.append({'Name': student[0], 'FamilyName': student[1], 'Age': student[2], 'CollegeName': student[3],
            'Student_id': student[4], 'Stream': student[5], 'ClassSection': student[6]})

        connection.close()
        return {'Students': Students}

        
