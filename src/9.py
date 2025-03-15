import random
def get_random_python_code():
    code = f"""
def {random.choice(["cool_func", "my_function"])}():
    {random.choice(["print('hello world')", "return 1 + 2"])}
"""
    return code