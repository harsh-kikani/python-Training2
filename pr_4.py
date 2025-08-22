import json

#--------------------Classes----------------------

class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, student_id, name, age, grade):
        super().__init__(student_id, name, age)
        self.grade = grade

class Teacher(Person):
    def __init__(self, teacher_id, name, age, subject):
        super().__init__(teacher_id, name, age)
        self.subject = subject

class Course:
    def __init__(self, course_id, title, teacher_id):
        self.course_id = course_id
        self.title = title
        self.teacher_id = teacher_id

class Enrollment:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id
        
        

#----------Data Storage-------

students = []
teachers = []
courses = []
enrollments = []
DATA_FILE = "school_management.json"

def save_data():   
    