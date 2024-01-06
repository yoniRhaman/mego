# class MyClass:
#     def __init__(self, value):
#         self._hidden_value = value   # single underscore for internal use
#         self.__hidden_value = value  # double underscore for name mangling

# def get_hidden_value(self):
#     return self._hidden_value  # direct access to the single underscore att.

# def get_secret_value(self):
#     return self._MyClass__hidden_value

# def __repr__(self):
#     return f"MyClass({self._hidden_value})"


# obj = MyClass(10)

# hidden_value = getattr(obj, "_MyClass__hidden_value")
# print(hidden_value)
# print(obj._hidden_value)   # not recommended (DON'T) (biden...)
# obj.__hidden_value = 2
# print(obj._hidden_value)
# obj._MyClass__hidden_value = 2
# print(obj)
# print(obj.__hidden_value)


# @class_method
# a user class with instance attributes and instance methods
class User:
    active_users = 0

    @classmethod  # decorator
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}, {self.first}"

    def __repr__(self):
        return f'{self.first} is {self.age} he/she likes {self.likes("j")}'
    #
    # def __str__(self):
    #     return f"Who am i??"


tom = User.from_string("Tom,Jones,89")
# print(tom)

j = User("jonah", "steele", 18)
# print(j)

j = str(j)  # you killed him...
print(j)
print(User.active_users)
tom.logout()
print(User.active_users)
print(tom.age)
tom.birthday()
print(tom.birthday())
print(tom.age)
print(tom.is_senior())
print(tom.likes("Pizza"))
print(tom.likes("m"))



