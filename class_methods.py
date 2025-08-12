class Employee:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        
e1 = Employee()
e1.name = "John"
e1.show()
e1.changeCompany("Google")
e1.show()
print(Employee.company)  

