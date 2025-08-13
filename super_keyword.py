class employee :
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class programmer(employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)  # Call the constructor of the parent class
        self.language = language
        
rahul = employee("Rahul", "101")
rohan = programmer("mehul", "102", "Python")
print(rohan.name)  
print(rohan.id)
print(rohan.language)
    