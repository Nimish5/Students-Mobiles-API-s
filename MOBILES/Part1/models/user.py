# Section6 - Video 93: Creating User & Item models

import sqlite3

class UserModel():

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("sqldata.db")
        cursor = connection.cursor()

        query = "SELECT * FROM Users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user