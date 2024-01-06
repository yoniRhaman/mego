# import datetime
# import pytz


# class Account:
#
#     @staticmethod
#     def _current_time():
#         utc_time = datetime.datetime.utcnow()
#         return pytz.utc.localize(utc_time)
#
#     ''' Simple account class with balance '''
#
#     def __init__(self, name, balance):
#         self._name = name
#         self.__balance = balance
#         self._transaction_list = []
#         print("Account created for " + self._name)
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
#             self.transaction_list.append((self._current_time(), amount))
#             self._transaction_list.append((Account._current_time(), amount))

    # def withdraw(self, amount):
    #     if self.__balance >= amount:  # to avoid being a millionaire...
    #         self.__balance -= amount
    #         self._transaction_list.append((Account._current_time(), -amount))
    #     else:
    #         print("The amount must be <= than the current balance, which is: {}".format(self.__balance))

    # def show_balance(self):
    #     print("Balance is: {}".format(self.__balance))
    #
    # def show_transactions(self):
    #     for date, amount in self._transaction_list:
    #         if amount > 0:
    #             tran_type = "deposited"
    #         else:
    #             tran_type = "withdrawn"
    #             amount *= -1
    #         print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


# chaim = Account("Chaim", 100)
# chaim.deposit(100)
# chaim.withdraw(200)
# chaim.show_transactions()
# chaim.show_balance()
# Function Signature -> name + parameter list + ret. val.
# Code Duplications
# DRY = Don't Repeat Yourself
# Static Methods (/functions)
# non-public (ksheyesh undersdcore mitahat lamishtane)
# Mangling
# shmuel = Account("Shmuel", 800)
# shmuel.deposit(100)
# shmuel.withdraw(200)
# shmuel.show_transactions()
# shmuel.show_balance()

# shmuel.__balance = 300

# shmuel._Account__balance = 300

# shmuel.show_balance()
# print(shmuel.__dict__)

'''
Write a class that represents a circle, and a method to calculate the area of the circle
# input: radius
'''


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * (self.radius ** 2)


radius = float(input("Enter the radius: "))
circle = Circle(radius)
print(circle.calculate_circle_area())






