#--------WHILE---------

#count = 1
#while count <= 5 :
#    print("hello" )
#    count += 1
    
#print(count)
#
#i = 1 
#while i <= 5:
#    print("how are you")
#    i+=1


#i = 1
#while i <= 100:
#    print(i)
#    i += 1

#i = 100
#while i >= 1:
#    print(i)
#    i -= 1
#print("loop ended")    
    

#n = int(input("Enter the number : "))
#i = 1
#while i <= 10:
#    print(n*i)
#    i += 1


#nums = [1, 4, 9, 16, 25, 40, 59, 79, 89, 100]
#heroes = ["ironman", "thor", "superman", "batman"]

#i = 0 
#while i < len(heroes):
#    print(heroes[i])
#    i += 1
    
    
#idx = 0
#while idx < len(nums):
#    print(nums[idx])
#    idx += 1


#-------------BREAK AND CONTINUE---------------

#nums = (1, 4, 9, 16, 25, 40, 59, 79, 89, 100, 25)
#x = 25
#i = 0
#while i < len(nums):
#    if(nums[i] == x):
#        print("FOUND at idx", i)
#        break#
#    else:
#        print("finding..")
#    i += 1
    
    
#i = 1
#while i <= 10:
#    if(i%2 != 0):
#        i += 1
#        continue
#    print(i)
#    i += 1
    
#-----------------FOR LOOP---------------------
#tup = (1, 2, 3, 5, 6, 8, 9)
#for num in tup:
#    print(num)
    
'''str = "helloworld"
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END")'''
    
    
    
'''nums = [1,4,9,16,25,36,49,64,81,100,36]
x = 36
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
    idx += 1'''
    

'''for i in range(1, 101):
    print(i)

for i in range(100, 0, -1):
    print(i)  '''

'''n = int(input("enter number : "))

for i in range(1, 11):
    print(n * i)'''


'''n = 7
sum = 0
for i in range(1, n+1):
    sum += i
print("total sum =", sum)

n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
    
print("total sum =", sum)'''



#------factorial-----
'''n = 7
fact = 1
i = 1
while i <= n :
    fact *= i 
    i+=1
print("factorial =", fact)

n =5 
fact = 1
for i in range(1, n+1):
    fact *= i
    
print("factorial =", fact)'''