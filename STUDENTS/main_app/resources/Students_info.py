from flask_restful import Resource, reqparse
from models.Students_info import ClassModel
from flask_jwt import jwt_required

class StudentClass(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('FamilyName', type=str, required=True, help='Mandatory Field!')
    parser.add_argument('Age', type=int, required=True, help='Mandatory Field!')
    parser.add_argument('CollegeName', type=str, required=True, help='Mandatory Field!')
    parser.add_argument('Student_id', type=str, required=True, help='Mandatory Field!')
    parser.add_argument('Stream', type=str, required=True, help='Mandatory Field!')
    parser.add_argument('ClassSection', type=str, required=True, help='Mandatory Field!')
    parser.add_argument('Store_id', type=int, required=True, help='Mandatory Field!')

    @jwt_required()
    def get(self, name):
        Student = ClassModel.Student_existance(name)
        if Student:
            return Student.json(), 200
        return f"The '{name}' dose not exist in the Students database!", 404

    def post(self, name):
        if ClassModel.Student_existance(name):
            return {'Messege': f'The Student {name} is already exist in the Students Database!'}

        data = StudentClass.parser.parse_args()

        Student = ClassModel(name, data['FamilyName'], data['Age'], data['CollegeName'], data['Student_id'], data['Stream'], data['ClassSection'], data['Store_id'])      

        try:
            Student.Save_to_db()
        except:
            return {'Messege': 'An error occured in saving a Student in the database table'}, 500

        return Student.json(), 201

    def put(self, name):
        data = StudentClass.parser.parse_args()

        Student = ClassModel.Student_existance(name)
        
        if Student is None:
            Student = ClassModel(name, data['FamilyName'], data['Age'], data['CollegeName'], data['Student_id'], data['Stream'], data['ClassSection'], data['Store_id'])          
        else:
            Student.FamilyName, Student.Age, Student.CollegeName, Student.Stream, Student.ClassSection = data['FamilyName'], data['Age'], data['CollegeName'], data['Stream'], data['ClassSection']     
            # We are updating 'Student_id' keeing it the same, if you want you can change it.
        
        Student.Save_to_db()
        return Student.json(), 201

    def delete(self, name):
        Student =  ClassModel.Student_existance(name)
        if Student:
            Student.delete_from_db()
        return {'Messege': f'The Student {name} is Deleted Succefully!'}


class All_Students(Resource):
    def get(self):
        return {'Students': [Student.json() for Student in ClassModel.query.all()]}
        # {'Students': list(map(lambda x: x.json(), ClassModel.query.all()))}


