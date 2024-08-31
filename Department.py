import CourseComponents
import Course
import Instructor
class Department():
    def __init__(self, name, CourseComponents):
        self.name = name
        self.courses = []
        self.instrctors = []
        self.CourseComponents = CourseComponents

    def add(self, component):
        if isinstance(component, Course):
            self.courses.appened(component)
        elif isinstance(component, Instructor):
            self.instrctors.append(component)

    def remove(self, component):
        if isinstance(component, Course):
            self.courses.remove(component)
        elif isinstance(component, Instructor):
            self.instrctors.remove(component)

    def display(self):
        print(f"Department: {self.name}")
        print(f"Courses:")
        for course in self.courses:
            print(f" - {course.name}")
        print("Instructors:")
        for instructor in self.instrctors:
            print(f" - {instructor.name}")

    def __str__(self):
        return f"Department: {self.name}, Courses: {self.courses}, Instructors: {self.instrctors}"