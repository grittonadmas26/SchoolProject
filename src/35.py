class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def print_data(self):
        if not self.data:
            print("No data to print.")
        else:
            for item in self.data:
                print(item)

# Example usage
my_class = MyClass()
data1 = [1, 2, 3]
data2 = ["a", "b", "c"]
my_class.add_data(data1)
my_class.add_data(data2)
my_class.print_data()
