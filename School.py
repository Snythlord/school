class School: 
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors  = []
        self.departments = []
        self.terms = []
    
    def register_student(self, student):
        self.students.append(student)

    def register_instructor(self, instructor):
        self.instructors.append(instructor)

    def register_department(self, department):
        self.departments.append(department)

    def create_term(self, term):
        self.terms.append(term)

    def generate_transcript(self, student):
        transcript =f" Transcript for {student.name} (ID: {student.id_number})\n"
        for term_name, courses in student.courses.items():
            transcript += f"Term: {term_name}\n"
            for course in courses:
                grade = course.grades.get(student.id_number, "N/A")
                transcript += f"Course: {course.name}, Grade: {grade}\n"
        return transcript

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

    def __str__(self):
        return f"School: {self.name}, Department: {[dept.name for dept in self.departments]}, Terms {[term.name for term in self.terms]}"