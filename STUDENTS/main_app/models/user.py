from db import db

class UserModel(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(50))
    Password = db.Column(db.String(50))

    def __init__(self, Username, Password):   # _id
        self.Username = Username
        self.Password = Password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(Username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def Save_Credentials_to_db(self):
        db.session.add(self)
        db.session.commit()


