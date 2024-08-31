from abc import ABC, abstractmethod
class GradingSystem(ABC):
    @abstractmethod
    def assign_grade(self, student, grade):
        pass

    @abstractmethod
    def get_grades(self):
        pass