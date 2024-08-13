import mysql.connector
from connection import conn


class Student:
    conn = conn
    mycursor = conn.cursor()

    def __init__(self, id, studentNumber, name, surname, birthdate, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate, Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql, value)

        try:
            Student.conn.commit()
            print(f"{Student.mycursor.rowcount} new record are added!")
        except mysql.connector.Error as err:
            print("Error: ", err)
        finally:
            Student.conn.close()
            print("Database connection is closed")

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate, Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql, values)

        try:
            Student.conn.commit()
            print(f"{Student.mycursor.rowcount} new record are added!")
        except mysql.connector.Error as err:
            print("Error: ", err)
        finally:
            Student.conn.close()
            print("Database connection is closed")

    @staticmethod
    def studentInfo():
        sql = "SELECT * FROM student"

        Student.mycursor.execute(sql)

        try:
            results = Student.mycursor.fetchall()
            print(results)
        except mysql.connector.Error as err:
            print("Error: ", err)
        finally:
            Student.conn.close()

    @staticmethod
    def getStudentById(id):
        sql = "SELECT * FROM student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql, value)

        try:
            return Student.mycursor.fetchone()
        except mysql.connector.Error as err:
            print("Error: ", err)
        finally:
            Student.conn.close()

    def updateStudent(self):
        sql = "UPDATE student SET studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender, self.id)
        Student.mycursor.execute(sql, values)

        try:
            Student.conn.commit()
            print(f"{Student.mycursor.rowcount} records are updated!")
        except mysql.connector.Error as err:
            print("Error: ", err)
        finally:
            Student.conn.close()

    @staticmethod
    def updateStudents(liste):
        sql = "UPDATE student SET studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1, 2, 3, 4, 5, 0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} records are updated!")
        except mysql.connector.Error as err:
            print("Error: ", err)
        finally:
            Student.conn.close()

    @staticmethod
    def getStudentsGender(gender):
        sql = "SELECT * FROM student WHERE gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql, value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("Error", err)



Student.studentInfo()
























