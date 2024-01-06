# from turtle import Turtle, Screen
#
#
# screen = Screen()
# screen.setup(width=500, height=400)  # overriding default values
# user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win? (enter a color): ")
# print(user_bet)
#
# colors = ["red", "green", "blue"]
# y_positions = [-70, -10, 50]
#
# for turtle_index in range(0, 3):
#     tim = Turtle(shape="turtle")
#     tim.color(colors[turtle_index])
#     tim.penup()
#     tim.goto(x=-230, y=y_positions[turtle_index])
#
#
# screen.exitonclick()
'''

1.
NameError
- When a certain name is not found
- example: print(qaswadefghnmmhgfds)

2.
ValueError
- You get an argument of the correct type, but has an invalid value
- example:
   import math
   print(math.sqrt(-10))

3.
TypeError
- when trying to use a method on an object of an inappropriate type
- ex:
   a = 12
   b = "3"
   print(a/b)

4.
SyntaxError
- When you write something which exists but is completely wrong

5.
ReferenceError
- When you are trying to "raise the dead"
  ...calling a "dead" object

6.
IndexError
- when you are out of bounds

7.
ModuleNotFoundError
- When you are (...still an invalid) trying to import something which does not exist

8.
AttributeError
- example:
  x = 10
  x.append(6)

Complete List:
https://docs.python.org/3/library/exceptions.html

SLICING
'''
parrot = "Norwegian"
print(parrot[0:6]) # Norweg

print(parrot[3:5])  # we

print(parrot[0:9]) # --> everything

print(parrot[:9])

print(parrot[2:])  # r...n

