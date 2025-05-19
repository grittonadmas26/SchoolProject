def square_root(num):
    if num < 0:
        raise ValueError("Cannot find square root of a negative number.")
    return int(num**0.5)

try:
    print(square_root(9))
except ValueError as e:
    print(e)
