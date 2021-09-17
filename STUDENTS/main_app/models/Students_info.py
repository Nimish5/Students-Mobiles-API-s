from db import db

class ClassModel(db.Model):

    __tablename__ = 'Students'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(65))
    FamilyName = db.Column(db.String(65))
    Age = db.Column(db.Integer)
    CollegeName = db.Column(db.String(50))
    Student_id = db.Column(db.Integer)
    Stream = db.Column(db.String(45))
    ClassSection = db.Column(db.String(30))

    Store_id = db.Column(db.Integer, db.ForeignKey('Stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, Name, FamilyName, Age, CollegeName, Student_id, Stream, ClassSection, Store_id):
        self.Name = Name
        self.FamilyName = FamilyName
        self.Age = Age
        self.CollegeName = CollegeName
        self.Student_id = Student_id
        self.Stream = Stream
        self.ClassSection = ClassSection
        self.Store_id = Store_id

    def json(self):
        return {'Name': self.Name, 'FamilyName': self.FamilyName, 'Age': self.Age, 'CollegeName': self.CollegeName, 
        'Student_id': self.Student_id, 'Stream': self.Stream, 'ClassSection': self.ClassSection}

    @classmethod
    def Student_existance(cls, name):
        return cls.query.filter_by(Name=name).first()

    def Save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        

