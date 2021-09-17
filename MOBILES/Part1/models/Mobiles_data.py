# Section6 - Video 93: Creating User & Item models

import sqlite3

class PhoneModel():

    def __init__(self, Name, Mobile, Company, Price, IMEI_No):
        self.Name = Name
        self.Mobile = Mobile
        self.Company = Company
        self.Price = Price
        self.IMEI_No = IMEI_No

    def json(self):
        return {'Name': self.Name, 'Mobile': self.Mobile, 'Company': self.Company, 'Price': self.Price, 'IMEI_No': self.IMEI_No}

    @classmethod
    def name_existance(cls, name):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Mobiles WHERE Name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        
        if row:
            return cls(*row)

    def storing(self):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "INSERT INTO Mobiles VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (self.Name, self.Mobile, self.Company, self.Price, self.IMEI_No))

        connection.commit()
        connection.close()

    def modify(self):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "UPDATE Mobiles SET Mobile=?, Company=?, Price=?, IMEI_No=? WHERE Name=?"
        cursor.execute(query, (self.Mobile, self.Company, self.Price, self.IMEI_No, self.Name))

        connection.commit()
        connection.close()
