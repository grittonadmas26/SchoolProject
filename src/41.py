import random

class SimpleSchoolProject:
    def __init__(self):
        self.students = []
    
    def add_student(self, name):
        if len(self.students) < 10:
            self.students.append(name)
            return True
        else:
            return False
    
    def remove_student(self, name):
        for student in self.students:
            if student == name:
                self.students.remove(student)
                break
        else:
            return "Student not found."
    
    def display_students(self):
        print("Students:")
        for student in self.students:
            print(f"{student}")

# Example usage:
school_project = SimpleSchoolProject()
print(school_project.add_student("Alice"))
print(school_project.add_student("Bob"))
print(school_project.display_students())
print(school_project.remove_student("Alice"))
