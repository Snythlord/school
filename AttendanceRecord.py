import AttendanceSystem
class AttendanceRecord:
    def __init__(self, course, AttendanceSystem):
        self.course = course
        self.attendance = []
        self.AttendanceSystem = AttendanceSystem


    def mark_attendance(self, date, status):
        self.attendance.append((date, status))

    def get_attendance(self):
        return self.attendance
    def __str__(self):
        return f"Attendance record for {self.course.name}: {self.attendance}"