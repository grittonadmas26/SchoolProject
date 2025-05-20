def add_numbers(a, b):
    """
    This function adds two numbers.
    
    Parameters:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
        
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

def calculate_total(numbers):
    """
    This function calculates the total of all the numbers in the list.
    
    Parameters:
        numbers (list of int or float): A list of numbers to be added.
        
    Returns:
        int or float: The total sum of all the numbers.
    """
    return sum(numbers)

def main():
    print("Please enter two numbers:")
    num1 = input()
    num2 = input()

    result = add_numbers(int(num1), int(num2))
    
    if isinstance(result, float) and result < 0:
        result = -result

    total = calculate_total([int(num1), int(num2)])
    print(f"The total is {total}.")
    
if __name__ == "__main__":
    main()
