# Section6 - # Video 95 - 99

from db import db

class PhoneModel(db.Model):
    __tablename__ = 'Mobiles'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(85))
    Mobile = db.Column(db.String(85))
    Company = db.Column(db.String(85))
    Price = db.Column(db.Float(precision=2))
    IMEI_No = db.Column(db.String(85))

    store_id = db.Column(db.Integer, db.ForeignKey('Stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, Name, Mobile, Company, Price, IMEI_No, store_id):
        self.Name = Name
        self.Mobile = Mobile
        self.Company = Company
        self.Price = Price
        self.IMEI_No = IMEI_No
        self.store_id = store_id

    def json(self):
        return {'Name': self.Name, 'Mobile': self.Mobile, 'Company': self.Company, 'Price': self.Price, 'IMEI_No': self.IMEI_No}

    @classmethod
    def name_existance(cls, name):
        return cls.query.filter_by(Name=name).first()

    def storing_modify(self):            # To save an item/ object in db(SQLAlchemy)
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


