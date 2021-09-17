import sqlite3

class StudentModel():
    
    def __init__(self, Name, FamilyName, Age, CollegeName, Student_id, Stream, ClassSection):
        self.Name = Name
        self.FamilyName = FamilyName
        self.Age = Age
        self.CollegeName = CollegeName
        self.Student_id = Student_id
        self.Stream = Stream
        self.ClassSection = ClassSection

    def json(self):
        return {'Name': self.Name, 'FamilyName': self.FamilyName, 'Age': self.Age, 'CollegeName': self.CollegeName,
        'Student_id': self.Student_id, 'Stream': self.Stream, 'ClassSection': self.ClassSection}

    @classmethod
    def Search_By_Name(cls, name):
        connection = sqlite3.connect('Mydatabasefile.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM Students WHERE Name=?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()

        if row:
            return cls(*row)

    
    def Save_to_Database(self):
        connection = sqlite3.connect('Mydatabasefile.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO Students VALUES (?,?,?,?,?,?,?)"
        cursor.execute(query, (self.Name, self.FamilyName, self.Age, self.CollegeName, self.Student_id, self.Stream, self.ClassSection))     

        connection.commit()
        connection.close()

    def Updation(self):
        connection = sqlite3.connect('Mydatabasefile.db')
        cursor = connection.cursor()

        query = "UPDATE Students SET FamilyName=?, Age=?, CollegeName=?, Student_id=?, Stream=?, ClassSection=? WHERE Name=?"  
        cursor.execute(query, (self.FamilyName, self.Age, self.CollegeName, self.Student_id, self.Stream, self.ClassSection, self.Name))      

        connection.commit()
        connection.close()

    def Delete_from_Database(self):
        connection = sqlite3.connect('Mydatabasefile.db')
        cursor = connection.cursor()

        query = "DELETE FROM Students WHERE Name=?"
        cursor.execute(query, (self.Name,))

        connection.commit()
        connection.close()
 
        