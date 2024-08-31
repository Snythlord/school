# class Discount:
#     def __init__(self, customer_type):
#         self.customer_type = customer_type

#     def apply_discount(self, amount):
#         if self.customer_type == "regular":
#             return amount * 0.9
#         if self.customer_type == "premium":
#             return amount * 0.8
#         return amount
from abc import ABC, abstractmethod
class Discount(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

class RegularDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.9

class PremiumDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.8