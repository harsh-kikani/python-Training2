'''import threading
import time
from concurrent.futures import ThreadPoolExecutor 

# indicate some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    
def main():
    time1 = time.perf_counter()
    # normal code
   ''' '''func(4)
    func(2)
    func(1)''''''


    # same code using threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # calculate time
    time2 = time.perf_counter()
    print(time2 - time1) 

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        print(future1.result())
        future2 = executor.submit(func, 2)
        print(future2.result())
        future3 = executor.submit(func, 4)
        print(future3.result()) 
        
poolingDemo()'''


import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Done!")
