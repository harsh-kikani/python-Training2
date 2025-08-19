#-----del-----

'''class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("rahul")
print(s1.name)
del s1.name
print(s1.name)'''


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


class Car:
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
print(car1.type)   

        



        