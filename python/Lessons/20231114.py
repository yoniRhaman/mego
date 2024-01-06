# import turtle as t
# tim = t.Turtle()
#
# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.color("red")
# timmy.pencolor("red")
# timmy.shape("turtle")
# timmy.forward(100)
#
'''
Your mission (5 minutes) is to:
Draw a black square, and show an arrow instead of a turtle 
'''
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
#
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)
'''
Ass. 2:
Draw a dashed line

'''
from turtle import Turtle, Screen

timmy = Turtle()
for _ in range(2):
    for _ in range(15):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()

    timmy.penup()
    timmy.forward(75)

screen = Screen()
screen.exitonclick()


