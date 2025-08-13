class person:
    def __init__(self, name, occ):
        print("hey in am a person")
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = person("Alice", "python developer")
b = person("vaishvanavi", "HR")
a.info()  # Alice is a python developer
b.info()  # vaishvanavi is a HR