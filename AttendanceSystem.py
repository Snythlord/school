from abc import ABC, abstractmethod
class AttendanceSystem(ABC):

    @abstractmethod
    def make_attendance(self, date, status):
        pass

    @abstractmethod
    def get_attendance(self):
        pass