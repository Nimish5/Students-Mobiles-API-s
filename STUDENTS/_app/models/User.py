import sqlite3

class UserModel():

    def __init__(self, _id, Username, Password):
        self.id = _id
        self.Username = Username
        self.Password = Password

    @classmethod
    def Search_By_Username(cls, Username):
        connection = sqlite3.connect('Mydatabasefile.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM Users WHERE Username=?'
        result = cursor.execute(query, (Username,))
        row = result.fetchone()

        if row:
            user_tuple = cls(*row)
        else:
            user_tuple = None

        connection.close()
        return user_tuple

    @classmethod
    def Search_By_id(cls, _id):
        connection = sqlite3.connect('Mydatabasefile.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM Users WHERE id=?'
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user_tuple = cls(*row)
        else:
            user_tuple = None
        
        connection.close()
        return user_tuple

    
