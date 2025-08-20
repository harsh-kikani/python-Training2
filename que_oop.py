class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("employee details :")
        print("role = ", self.role)
        print("department=",self.dept)
        print("salary=",self.salary)
    
name = input("Enter employee name :")
role = input("Enter employee role :")
dept = input("Enter employee dept :") 
salary = input("Enter employee salary :")


emp = Employee(role, dept, salary)

print("\nEmployee Details:")
emp.showDetails()


print("\nType of object:")
print(type(emp))



