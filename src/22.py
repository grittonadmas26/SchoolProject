def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [10.5, 20.7, 30.8]
average = calculate_average(numbers)
print("The average of the given numbers is:", average)
