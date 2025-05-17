def print_rangoli(size):
    # Generate a list of square patterns with alternating 'x' and '-' symbols
    squares = [''.join(('-', c) * i)
               for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')
               if (i + 1) % 2 != 0]

    # Convert each square into a string and add '-' between them to form the pattern
    patterns = [''.join(p).lower() for p in squares]
    patterns.extend(squares)

    # Join all the patterns together to get the final output
    print('-'.join(patterns[::-1]))

# Example usage:
print_rangoli(size=7)
