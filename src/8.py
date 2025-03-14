import random

def get_random_number(max_value):
    return random.randint(0, max_value)

def print_hello():
    print("Hello World")

if __name__ == "__main__":
    number = get_random_number(10)
    print(f"The random number is {number}")
