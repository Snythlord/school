import Course
import Department
import Instructor
import Student
import Term
import School
import Grade

school = School.School("University of michigan")


math_department = Department("Mathematics")
science_department = Department("Science")

school.register_department(math_department)
school.register_department(science_department)

instructor1 = Instructor.Instructor("Dr. Brown", "I001")
math_department.add(instructor1)

fall_term = Term("Fall 2022", "2024-09-01", "2024-12-20")
school.create_term(fall_term)

course1 = Course("Math 101", "MTH101", instructor1)
course2 = Course("Math 201", "MTH201", instructor1, prereuquisites =[course1])
math_department.add(course1)
math_department.add(course2)
fall_term.add_course(course1)
fall_term.add_course(course2)


student1 = Student("Alice Johnson", "123456789")
student2 = Student("Bob Smith", "987654321")

fall_term.enroll(student1)
fall_term.enroll(student2)

course1.assign_grade(student1, Grade("A"))
course1.assign_grade(student2, Grade("B"))


student1.attendance[course1.course_code].mark_attendance("2024-09-01", "Present")
student2.attendance[course1.course_code].mark_attendance("2024-09-01", "Absent")

math_department.display()

print(school.generate_transcript(student1))
