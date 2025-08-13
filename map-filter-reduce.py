# MAP

#def cube(x):
#    return x*x*x

#print(cube(2))
#l = [1, 2, 4, 6, 5,3]
'''newl = []
for item in l:
    newl.append(cube(item))'''
  
#newl = list(map(cube, l))
#print(newl)   

# FILTER

#def filter_function(a):
#    return a > 2
#newnewl = list(filter(fil ter_function, l))
#print(newnewl)


#==========================================================
#lambda

#l = [1, 2, 4, 6, 5, 3]
#newl = list(map(lambda x: x*x*x, l))
#print(newl)

 
#def filter_function(a):
#    return a > 2
#newnewl = list(filter(filter_function, l))
#print(newnewl)

#reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]
# calculate the sum of all numbers using reduce function

def mysum(x, y):
    return x + y
sum = reduce(mysum, numbers)

print(sum)