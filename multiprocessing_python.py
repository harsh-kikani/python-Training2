import multiprocessing
import time

def square_numbers():
    for i in range(5):
        print(f"{i} squared is {i * i}")
        time.sleep(1)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=square_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")

