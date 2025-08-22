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
    
 
#import os
#os.remove("myfile2.txt")


'''with open("myfile2.txt", "w") as f:
    f.write("Hii everyone\nWe are learning File I/O\n")
    f.write("using python.\nI like programming in python")'''
    
    
#--------read()----replace()---------    

'''with open("myfile2.txt", "r") as f:
    data = f.read()


new_data = data.replace("python","Django")
print(new_data)

with open("myfile.txt", "w") as f:
    f.write(new_data)'''

    
#------------find()----------------

'''def check_for_word():
    word = "nolearning"
    with open("myfile.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")
            
check_for_word()'''


#-----------readline()-----------------

'''def check_for_word():
    word = "nolearning"
    with open("myfile.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("myfile.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        
    return -1
print(check_for_line())  '''


count = 0
with open("myfile3.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)