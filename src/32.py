import random

def find_prime_numbers(limit):
    """
    Find prime numbers up to a given limit.
    
    Args:
        limit (int): The upper limit for generating prime numbers.
        
    Returns:
        list: A list of prime numbers up to the given limit.
    """
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

limit = 30
prime_numbers = find_prime_numbers(limit)
print(f"The prime numbers up to {limit} are: {prime_numbers}")
