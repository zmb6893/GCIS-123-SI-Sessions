"""
Time complexity activities. Go to quicksort.py for more practice.
@author: Zoe Bingham
"""
def hello():
    # What is my time complexity?
    print("hello")
    print("goodbye")

def for_loop(n=3):
    # What is my time complexity?
    for _ in range(n):
        print("hello")
        print("goodbye")

def two_for_loop(n=3):
    # What is my time complexity?
    for _ in range(n):
        print("hey")
    for _ in range(n):
        print("bye")

def nested_for_loop(n=3):
    # What is my time complexity?
    for _ in range(n):
        print("hello")
        for _ in range(n):
            print("hello")
        print("goodbye")
        for _ in range(n):
            print("goodbye")

def recurse(iteration = 3):
    # What is my time complexity?
    if(iteration == 0):
        return
    print("hello %d"%iteration)
    recurse(iteration-1)

def main():
    hello()
    print()
    for_loop()
    print()
    two_for_loop()
    print()
    nested_for_loop()
    print()
    recurse()

if __name__ == "__main__":
    main()