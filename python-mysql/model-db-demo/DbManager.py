import mysql.connector
from connection import conn
from Student import Student
from Teacher import Teacher


class DbManager:
    def __init__(self):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def getStudentById(self, id):
        sql = "SELECT * FROM student WHERE id = %s"
        value = (id,)

        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def getStudentByClassId(self, classid):
        sql = "SELECT * FROM student WHERE classid = %s"
        value = (classid,)

        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def deleteStudent(self, studentid):
        sql = "DELETE FROM Student WHERE id=%s"
        value = (studentid,)
        self.cursor.execute(sql, value)

        try:
            self.conn.commit()
            print(f"{self.cursor.rowcount} record is deleted!")
        except mysql.connector.Error as err:
            print("Error: ", err)

    def getClasses(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.createClass(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate, Gender, ClassId) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, value)

        try:
            self.conn.commit()
            print(f"{self.cursor.rowcount} new record are added!")
        except mysql.connector.Error as err:
            print("Error: ", err)

    def editStudent(self, student: Student):
        sql = "UPDATE student SET studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        Student.mycursor.execute(sql, value)

        try:
            self.conn.commit()
            print(f"{self.cursor.rowcount} record is updated!")
        except mysql.connector.Error as err:
            print("Error: ", err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    # will be executed when obj is deleted
    def __del__(self):
        self.conn.close()
        print("Db connection is closed!")


db = DbManager()

# db.getStudentById(7)
# print(student[0].name)
# print(student[0].surname)

students = db.getStudentByClassId(1)





