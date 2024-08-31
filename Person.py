from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name, id_number):
        self.name = name
        self.id_number = id_number

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):

        return f"Name: {self.name}\ ID: {self.id_number}"
