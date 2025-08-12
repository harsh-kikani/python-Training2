class employee:
    companyName = "Apple"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 1.04   
        
    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")
        
#employee.showDetails(emp1)
emp1 = employee("John")
emp1.raise_amount = 2.3
emp1.companyName = "Google"
emp1.showDetails() 
employee.companyName = "Microsoft"
print(employee.companyName)   

emp2 = employee("Alice")   
emp2.companyName = "Amazon"
emp2.showDetails()