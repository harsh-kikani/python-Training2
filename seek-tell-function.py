'''with open ('myfile.txt', 'r') as f:
    print(type(f))
    # move to the 10th byte in the file
    
    f.seek(10)
    
    #read the next 5 bytes
    data = f.read(5)
    print(data)'''
    
'''with open('myfile.txt', 'r') as f:
    print(type(f))
    # move to the 10th byte in the file
    
    f.seek(10)
    
    #read the next 5 bytes
    print(f.tell())  
    data = f.read(5)
    print(data)'''
    
with open('sample.txt', 'w') as f:
    f.write("hello world")
    f.truncate(3)
    
with open('sample.txt', 'r') as f:
    print(f.read())  # Output: hel