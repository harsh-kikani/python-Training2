#class employee:
#    def __init__(self):
#        self.__name = "John"
        
#a = employee()
# print(a.__name)  # cannot be accessed directly

#print(a._employee__name)  # can be accessed indirectly
 
#print(a.__dir__())


class student:
    def __init__(self):
        self._name = "harsh"
        
    def _funname(self):            # protected method
        
        return "hello world"

class subject(student):           
    pass                          #inherited class

obj = student()
obj1 = subject()

# calling by object of student class
print(obj._name)
print(obj._funname())  # hello world

# calling by object of subject class
print(obj1._name)  
print(obj1._funname())  # hello world