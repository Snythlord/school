import Person
class Student(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self.courses = []

    def enroll(self, course):
        self.courses.appened(course)

    def __str__(self):
        courses_str = ", ".join([course.name for course in self.courses])
        return f"Student {self.name} with ID number {self.id_number} enrolled in {courses_str}"
    
