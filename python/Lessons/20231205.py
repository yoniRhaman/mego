'''
SYNTAX ERRORS
def first:
None = 1
;
return

NAME ERRORS
test

TYPE ERRORS
len(3)
"I am cool" + []     
3 + 's'
len(4.3)
print(len(4.3))

INDEX ERRORS
list = ["hello"]
print(list[1])

VALUE ERRORS
print(int("23s"))

KEY ERRORS
d = {}
d["foo"]

Attribute Errors
"cool".jojo()

"".joint(['a','b'])
'''

# raise ValueError("invalid value")
# throw an error
# print("hi")


# def colorize(text, color):
#     colors = ("cyan", "yellow", "blue", "green", "magenta")
#     if type(text) is not str:
#         raise TypeError("Text must be a string. (don't be an invalid)")
#     elif color not in colors:
#         raise ValueError(f"Sorry, the color: {color} you chose is invalid.")
#         # raise Exception   (NOT READABLE)
#     else:
#         print(f"Printed {text} in {color}")
#
#
# colorize([], 10)

# exception handling
# try-except blocks

# try:
#     foobar
# except NameError as err:
#     print("You tried to use a variable that was never declared!")
# print("After the 'try'... ")

d = {"Name": "Ricky"}
# d["city"]


# def get(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         err_str = "There is a key error my lord"
#         print(err_str)
#         return None
#
#
# get(d, "city")

# try
# except
# else
# finally

# while True:
#     try:
#         num = int(input("Please enter a number: "))
#     except ValueError:
#         print("That's not a number!")
#     else:
#         print("Good job, you entered a number")
#         break
#     finally:
#         print("RUNS NO MATTER WHAT!")
#         print(name)
# print("Rest of the game logic still runs...")


