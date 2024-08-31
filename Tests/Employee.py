# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def calculate_pay(self):
#         pass

#     def save_to_database(self):
#         pass

#     def __str__(self):
#         return f"Name: {self.name}\ ID: {self.id_number}"
    
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_pay(self):
        pass

    
class EmployeeRepository:
    def save_to_database(self, employee):
        pass

# Second one is cleaner than the first
# Also first has problems because if people that are employees and are in different catagories
# try to access
# the same method they will get an error and it will be messy
# The second one is cleaner and more pythonic. It is also more object oriented. It is
# easier to read and understand and it is easier to debug
