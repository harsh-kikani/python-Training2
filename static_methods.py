class math:
    def __init__(self, num):
        self.num = num
        
    def addtonum(self, n):
        self.num = self.num + n
        
    @staticmethod
    def add(a, b):
        return a + b
    
# result = math.add(1 ,2)
# peint(result)  # output: 3
a = math(5)
print(a.num)  
a.addtonum(6)
print(a.num)  

print(math.add(7, 8))  