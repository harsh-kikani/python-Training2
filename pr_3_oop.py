#-----del-----

'''class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("rahul")
print(s1.name)
del s1.name
print(s1.name)'''

#---------------------
'''class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 =  Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())'''


#------ Private attributes & methods-------

'''class Person:
    __name = "anonymous"
    
    def __hello(self):
        print("hello person!")
        
    def welcome(self):
        self.__hello()
        
p1 = Person() 

print(p1.welcome())'''


#----Inherits-------

'''class Car:
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped.")
        
class ToyotaCar(Car):
    def __init__(self, brand):
        self.name = brand
        
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        
car1 = Fortuner("diesel")
car1.start()'''
        
        
#-----super() method---------


'''class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.name)   
print(car1.type)'''   

#----------------------class method--------------------
'''class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
        
    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
        
stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 88
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)'''

#-------------------------------------------------

'''class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
        
stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 88
print(stu1.percentage)'''

#---------------------------------------
        
'''class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
        
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img 
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img 
        return Complex(newReal, newImg)
    
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num1.showNumber()

num3 = num1 - num2
num3.showNumber()'''
    
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius **2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())
 


        