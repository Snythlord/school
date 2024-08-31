import CourseComponents
import GradingSystem
class Course():
    def __init__(self, name, course_code, instructor, prerequisites, CourseComponents, GradingSystem):
        self.name = name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []
        self.grades = {}
        self.prerequisites = prerequisites if prerequisites else []
        self.CourseComponents = CourseComponents
        self.GradingSystem = GradingSystem

    def add(self, student):
        if all(course in student.courses.values for course in self.prerequisites):
            self.students.append(student)
            self.grades[student.id_number] = None
        else:
            print(f"{student.name} does not meet the prerequisites for {self.name}.")

    def assign_grade(self, student, grade):
        if student.id_number in self.grades:
            self.grades[student.id_number] = grade
        else:
            print(f"{student.name} is not in {self.name}.")

    def remove(self, student):
        if student in self.students:
            self.students.remove(student)
            del self.grades[student.id_number]
    
    def display (self):
        print(f"Course: {self.name}, Code: {self.course_code}, Instructor {self.instructor}, Prerequisites: {self.prerequisites}")

    def get_grades(self):
        return self.grades