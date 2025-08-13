'''info = {'name':'rahul', 'age':21, 'eligible':True}

#print(info)
#print (info.keys())
#print (info.values())

#for key in info.keys():
 #   print(f"{key}:{info[key]}")
    
print (info.items())
for key, value in info.items():
   print(f"{key}:{value}")'''
   
emp1 = {122:45, 123:50, 124:60 , 125:70}
emp2 = {222:78, 222:90}

#emp1.update(emp2) # Merging two dictionaries
#emp1.clear() 
#emp1.pop(122) # Removing a key-value pair
emp1.popitem() 
del emp1[122] 
print(emp1)