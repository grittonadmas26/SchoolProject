import random

def get_random_number(n):
    return random.randint(1, n)

def main():
    num = get_random_number(20)
    print(num)

main()
