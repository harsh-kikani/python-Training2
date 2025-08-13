x=10  #global variable

def my_function():
    global x
    x=5 
    y=5 #local variable
    
my_function()
print(x)  