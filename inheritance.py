class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")
        
class programmer(employee):
    def showDetails(self):
        print("the default laughter is python")
        
        
e1 = employee("Alice", 101)
e1.showDetails()  # The name of employee: 101 is Alice
e2 = programmer("Bob", 102)
e2.showDetails()  # the default laughter is python

