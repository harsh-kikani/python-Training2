'''f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close()'''


f = open('myfile.txt', 'a')
f.write("hello word!")
f.close()

with open('myfile.txt', 'a') as f:
    f.write("hey i am inside with")