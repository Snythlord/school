class School: 
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors  = []
        self.courses = []
    
    def register_student(self, student):
        self.students.append(student)

    def register_instructor(self, instructor):
        self.instructors.append(instructor)

    def register_course(self, course):
        self.courses.append(course)

    def find_student_by_id(self, id_number):
        for student in self.students:
            if student.id_number == id_number:
                return student.name
        return None
    
    def find_instructor_by_id(self, id_number):
        for instructor in self.instructors:
            if instructor.id_number == id_number:
                return instructor.name
        return None

