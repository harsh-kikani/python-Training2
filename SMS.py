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


#---------------File Operations------------------
def save_data():   
    data = {
        "students": [vars(s) for s in students],
        "teachers": [vars(t) for t in teachers],
        "courses": [vars(c) for c in courses],
        "enrollments": [vars(e) for e in enrollments], 
    }
    with open("school_management.json", "w") as f:
        json.dump(data, f ,indent=4)
    print("Data save successfully.")
    
def load_data():
    try:
        with open("school_management.json", "r") as f:
            data = json.load(f)
            students.extend(students(**s) for s in data["students"])
            teachers.extend(teachers(**t) for t in data["teachers"])
            courses.extend(courses(**c) for c in data["courses"])
            enrollments.extend(enrollments(**e) for e in data["enrollments"])
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("No data found.")


#----------CRUD Operations---------------

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    students.append(Student(sid, name, age, grade))
    print("Student added.")

def add_teacher():
    tid = input("Enter Teacher ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    subject = input("Enter Subject: ")
    teachers.append(Teacher(tid, name, age, subject))
    print("Teacher added.")

def add_course():
    cid = input("Enter Course ID: ")
    title = input("Enter Course Title: ")
    tid = input("Enter Assigned Teacher ID: ")
    courses.append(Course(cid, title, tid))
    print("Course added.")

def enroll_student():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")
    enrollments.append(Enrollment(sid, cid))
    print("Student enrolled.")
        

#----------View and Reports--------------

def view_records():
    print("\n--- Students ---")
    for s in students:
        print(vars(s))
    print("\n--- Teachers ---")
    for t in teachers:
        print(vars(t))
    print("\n--- Courses ---")
    for c in courses:
        print(vars(c))
    print("\n--- Enrollments ---")
    for e in enrollments:
        print(vars(e))
        
        
def generate_reports():
    print("\nList of All Students")
    for s in students:
        print(f"{s.person_id} - {s.name} (Grade: {s.grade})")

    print("\nList of Teachers with Subjects")
    for t in teachers:
        print(f"{t.person_id} - {t.name} (Subject: {t.subject})")

    print("\nEnrollments")
    for e in enrollments:
        student = next((s.name for s in students if s.person_id == e.student_id), "Unknown Student")
        course = next((c.title for c in courses if c.course_id == e.course_id), "Unknown Course")
        print(f"{student} is enrolled in {course}")

#-------------Main Menu---------------

def main():
    load_data()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. View Records")
        print("6. Generate Reports")
        print("7. Save")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_teacher()
        elif choice == "3":
            add_course()
        elif choice == "4":
            enroll_student()
        elif choice == "5":
            view_records()
        elif choice == "6":
            generate_reports()
        elif choice == "7":
            save_data()
        elif choice == "8":
            save_data()
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
        
        
        
        
        


    
    