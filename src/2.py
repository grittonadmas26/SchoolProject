import random

def get_random_number(n):
    return random.randint(1, n)

def get_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += letters[random.randint(0, len(letters) - 1)]
    return result

def get_random_boolean():
    return random.choice([True, False])

def get_random_tuple(size):
    return tuple(random.sample(range(10), size))

def get_random_list(size):
    return list(random.sample(range(10), size))

def get_random_set(size):
    return set(random.sample(range(10), size))
