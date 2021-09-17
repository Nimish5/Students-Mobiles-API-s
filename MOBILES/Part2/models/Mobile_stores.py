# Section6 - # Video 102 

from db import db

class StoreModel(db.Model):
    __tablename__ = 'Stores'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(85))

    Mobiles = db.relationship('PhoneModel', lazy='dynamic')

    def __init__(self, Name):
        self.Name = Name

    def json(self):
        return {'Name': self.Name, 'Mobiles': [Mobile.json() for Mobile in self.Mobiles.all()]}

    @classmethod
    def name_existance(cls, name):
        return cls.query.filter_by(Name=name).first()

    def storing_modify(self):            # To save an item/ object in db(SQLAlchemy)
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


