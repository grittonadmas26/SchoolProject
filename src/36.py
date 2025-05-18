def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

school_projects_data = [10.5, 20.8, 30.9, 40.0]
average_grade = calculate_average(school_projects_data)
print("Average grade:", average_grade)
