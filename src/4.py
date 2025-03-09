def get_random_string(length):
    import random
    import string
    letters = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_integer(start, end):
    import random
    return random.randint(start, end)

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
