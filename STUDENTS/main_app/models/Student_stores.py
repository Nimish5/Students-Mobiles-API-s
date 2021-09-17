# Section 6: Video 102(Creating a new model: StoreModel)

from db import db

class StoreModel(db.Model):
    
    __tablename__ = "Stores"

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))

    Students_list = db.relationship('ClassModel', lazy='dynamic')

    def __init__(self, Name):
        self.Name = Name

    def json(self):
        return {'Name': self.Name, 'Students': [Student.json() for Student in self.Students_list.all()]}

    @classmethod
    def find_by_StoreName(cls, name):
        return cls.query.filter_by(Name=name).first()

    def Save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def Delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    
