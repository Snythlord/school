import Person
class Instructor(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self.courses = []

    def assign_courses(self, course):
        self.courses.append(course)

    def __str__(self):
        courses_str = ", ".join([course.name for course in self.courses])
        return f"Instructor {self.name} with ID number {self.id_number} teaching {courses_str}"

