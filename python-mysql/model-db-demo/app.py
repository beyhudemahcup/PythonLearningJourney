from DbManager import DbManager


class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Student List\n2-Add a new Student\n3-Update a Student\n4-Delete a Student\n5-Add a Student\n6-Lessons by Class\n7-Exit(Y/N)"
        while True:
            print(msg)
            user_input = input("Your input: ")
            if user_input == '1':
                self.displayStudents()
            elif user_input == '2':
                self.addStudent()
            elif user_input == '3':
                self.editStudent()
            elif user_input == '4':
                self.deleteStudent()
            elif user_input == 'Y' or user_input == 'N':
                break
            else:
                print("Invalid input, please enter correct data!")

    def addStudent(self):
        self.displayClasses()

        classid = int(input('What is your class number? : '))
        number = input('Student Id : ')
        name = input('Name : ')
        surname = input('Surname : ')
        year = int(input('Year : '))
        month = int(input('Month : '))
        day = int(input('Day : '))
        birthdate = datetime.date(year, month, day)
        gender = input('Gender (M/F) (sorry for only two genders :( )')

        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):
        self.displayClasses()
        classid = int(input('What is your class number? : '))

        students = self.db.getStudentsByClassId(classid)
        print("Student List")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        return classid

    def deleteStudent(self):
        classid = self.displayStudents()
        studentId = int(input('Student Id : '))

        self.db.deleteStudent(studentId)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Student Id : "))
        student = self.db.getStudentById(studentid)

        student[0].name = input("Name : ") or student[0].name
        student[0].surname = input('Surname :') or student[0].surname
        student[0].gender = input('Gender (M/F) :') or student[0].gender
        student[0].classid = input('Class : ') or student[0].classid

        year = input("Year : ") or student[0].birthdate.year
        month = input("Month : ") or student[0].birthdate.month
        day = input("Day : ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year, month, day)
        self.db.editStudent(student[0])













