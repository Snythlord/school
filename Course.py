class Course:
    def __init__(self, name, course_code, instructor):
        self.name = name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []
        self.grades = {}

    def add_student(self, student):
        self.students.append(student)
        self.grades[student.id_number] = None

    def assign_grade(self, student, grade):
        if student.id_number in self.grades:
            self.grades[student.id_number] = grade
        else:
            print(f"{student.name} is not in {self.name}.")

    def __str__(self):
        return f"Course: {self.name}, Code: {self.course_code}, Instructor {self.instructor}"