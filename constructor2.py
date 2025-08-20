'''class Student:
     def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("karan", 96)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)'''
         
'''class Student:
    college_name = "ABC..college"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student,", self.name)
        
    def get_marks(self):
        return self.marks

s1 = Student("karan", 97)
s1.welcome()
print(s1.get_marks()) '''  

# ------ABSTRACTION-------

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")
        
car1 = Car()
car1.start()

         
         
          