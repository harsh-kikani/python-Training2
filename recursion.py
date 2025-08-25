'''def factorial(n):
    if(n==1  or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")'''


'''def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")

show(8)'''

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)