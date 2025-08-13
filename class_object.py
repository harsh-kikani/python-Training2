class person:
    name = "John"
    occupation = "python developer"
    networth = 100000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
        
a = person()
b = person()
c = person()

a.name = "Alice"
a.occupation = "Data Scientist"

b.name = "Bob"
b.occupation = "Web Developer"

a.info()  # Alice is a Data Scientist
b.info()  # Bob is a Web Developer
c.info()  # John is a python developer