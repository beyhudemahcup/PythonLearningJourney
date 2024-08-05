def calculate_grades(line):
    letter_grade = ""
    line = line[:-1]
    grades_list = line.split(":")
    student_name = grades_list[0]
    grades = grades_list[1].split(',')

    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    grade_average = (grade1 + grade2 + grade3) / 3
    if 90 <= grade_average <= 100:
        letter_grade = "AA"
    elif 85 <= grade_average <= 89:
        letter_grade = "BB"
    elif 65 <= grade_average <= 85:
        letter_grade = "CC"
    elif 50 <= grade_average <= 65:
        letter_grade = "DD"
    else:
        letter_grade = "FF"
    return f"{student_name} : {letter_grade} \n"


def read_grades():
    with open("Exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grades(line))


def enter_grades():
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    grade = input("Grade 1: ")
    grade2 = input("Grade 2: ")
    grade3 = input("Grade 3: ")

    with open("Exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} {surname} : {grade}, {grade2}, {grade3}\n")


def save_grades():
    with open("Exam_grades.txt", "r", encoding="utf-8") as file:
        grades_list = []

    for i in file:
        grades_list.append(calculate_grades(i) + "\n")

    with open("Grades_results.txt", "w", encoding="utf-8") as file_results:
        for i in grades_list:
            file_results.write(i)


while True:
    user_input = input("1-Read your grades\n2-Enter a grade\n3-Save your grade\n4-Exit")

    if user_input == '1':
        read_grades()
    elif user_input == '2':
        enter_grades()
    elif user_input == '3':
        save_grades()
    else:
        break
