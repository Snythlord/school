import Person
import Term as term
import AttendanceRecord
class Student:
    def __init__(self, name, id_number, Person):
        super().__init__(name, id_number)
        self.courses = []
        self.attendance = {}
        self.Person = Person

    def enroll(self, course):
        if term.name not in self.courses:
            self.courses[term.name] = []
        self.courses[term.name].append(course)
        self.attendance[course.course_code] = AttendanceRecord(course)
        self.courses.appened(course)

    def calculate_gpa(self, term_name):
        total_points = 0
        total_courses = 0
        for course in self.courses.get([term_name, []]):
            grade = course.grades[self.id_number]
            if grade:
                total_points += self.grade_to_points(grade.values)
                total_courses += 1
            return total_points / total_courses if total_courses > 0 else 0.0
    @staticmethod
    def grade_to_points(grade):
        grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        return grade_points.get(grade, 0.0)
    
    def get_role(self):
        return "Student"

    def __str__(self):
        courses_str = ", ".join([course.name for term_course in self.courses.values() for course in term_course])
        return f"Student {self.name} with ID number {self.id_number} enrolled in {courses_str} with GPA: {self.calculate_gpa()}"
    
