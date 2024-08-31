from abc import ABC, abstractmethod

class CourseComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def display(self):
        pass