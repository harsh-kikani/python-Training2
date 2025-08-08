info = {'name':'rahul', 'age':21, 'eligible':True}

#print(info)
#print (info.keys())
#print (info.values())

#for key in info.keys():
 #   print(f"{key}:{info[key]}")
    
print (info.items())
for key, value in info.items():
   print(f"{key}:{value}")