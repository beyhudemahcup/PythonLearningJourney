# class
class Person:
    # class attributes (sets every instance's address as Istanbul)
    address = "Istanbul"

    # constructor
    def __init__(self, name, year):  # it will run for every instance we created
        # object attributes
        self.name = name
        self.year = year
        # print('init method run')

    # this is instance method, so we need to add 'self' as a parameter
    def intro(self):
        print(f"hello, My name is {self.name}")

    # this is instance method
    def calculateAge(self):
        return 2024 - self.year


# object, instance
p1 = Person('Mert', 2001)
p2 = Person('Cemil', 1994)

# updating
p1.name = 'Memil'
p2.year = 1984
p2.address = 'Balikesir'

# access object attributes
print(f"p1: name: {p1.name}, year: {p1.year}, address: {p1.address}, age is: {p1.calculateAge()}")
print(f"p2: name: {p2.name}, year: {p2.year}, address: {p2.address}, age is: {p2.calculateAge()}")
p1.intro()


class Circle:
    # class object attribute
    pi = 3.14

    # constructor
    def __init__(self, radius=1):
        self.radius = radius

    # methods
    def find_circumference_circle(self):
        return 2 * self.pi *9+ self.radius

    def find_area_circle(self):
        return self.pi * (self.radius ** 2)


c1 = Circle()  # radius = 1
c2 = Circle(5)

print(f"c1 : area = {c1.find_area_circle()}, circumference = {c1.find_circumference_circle()}")
print(f"c2 : area = {c2.find_area_circle()}, circumference = {c2.find_circumference_circle()}")