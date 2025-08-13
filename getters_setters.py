class myclass:
    def __init__(self, value):
        self._value = value
        
    def show (self):
        print(f"The value is {self._value}")
        
    @property
    def ten_value(self):
        return self._value * 10
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10
        
obj = myclass(10)
obj.ten_value = 67
print(obj.ten_value)  # This will raise an error since ten_value is not defined
obj.show()  # This will raise an error since show is not defined