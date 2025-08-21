'''f = open("myfile.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()'''


'''f = open("myfile.txt", "r")
data = f.read()
print(data)

l1 = f.readline()
print = (l1)

l2 = f.readline()
print = (l2)

f.close()'''



'''f = open("myfile.txt", "a")

f.write("then i will remove django")

f.write("\nafter the nodejs ")

f.close()
'''
 
'''with open("myfile.txt", "r") as f:
    data = f.read()
    print(data)
    
with open("myfile.txt", "w") as f:
    f.write("new data")'''
    
 
import os

os.remove("myfile2.txt")