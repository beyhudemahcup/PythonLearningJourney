# inheritance example

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("person created!!")

    def who_am_I(self):
        print("I am a Person")

    def eat(self):
        print("I am eating")


class Student(Person):  # extends to Person class
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print("student created!!")

    # override
    def who_am_I(self):
        print("I am a Student")


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_I(self):
        print(f"I am a {self.branch} Teacher")


p1 = Person("metin", "cetin")
s1 = Student("cetin", "ceviz")
t1 = Teacher("james", "yerli", "history")


print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)
print(t1.firstName + ' ' + t1.lastName+ ' '+ t1.branch)

p1.who_am_I()
s1.who_am_I()
t1.who_am_I()

p1.eat()
s1.eat()
