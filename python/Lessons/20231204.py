# Sets are unordered collections of unique elements
# Sets do not have indices (plural of index)
# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(2)
# yourSet = {1,2,3}
# print(myset)

# mylist = [1, 12, 1, 1, 2, 2, 3, 3, 3, 3]
# myset2 = set(mylist)
# print(myset2)

# lists []
# dictionaries {key:"value"}
# tuples ()
# sets {}

# pep talk

# File System

# file = open("my_file.txt")
# contents = file.read()
# print(type(contents))
# file.close()

# close the file when done with the block
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

### BAD !!!
# w for write
# with open("my_file.txt", mode="r+") as file:
#     contents = file.read()
#     print(contents)
#     file.write("33")
#     print(contents)
###
'''
r - reading
w - writing
r+ - read & write
w+ - writing, creates a new file if doesn't exist
a - writing, appending, creates...
a+ - read, write, append, creates...
x - created only if does not exist, writing...
    aka "exclusive creation"
'''

# with open("my_fi.txt", mode="r+") as file:
#     file.write("I am Groot!")
#     the cursor moves to the end of the string!!!
    #
    # that is why the following code printed "nothing"
    # contents = file.read()
    # print(contents)
#
# with open("my_fi.txt") as file:
#     contents = file.read()
#     print(contents)
'''
Relative and Absolute file paths

Absolute file path - examples:
C:/work/project/my_file.py
C:/work/project/report.docx

Relative file path
./my_file.py

working directory (the current folder you're working from)
./     = current folder, used for relative paths

current -> C:\work
in order to get to myfile, using relative path, we'll write:
./project/my_file.py

in order to get to report file, using relative path, we'll write:
./project/report.docx

#'''
#str = r"C:\Users\eyal1\PycharmProjects"

# current working dir.: C:\Users\eyal1\PycharmProjects\pythonProject

# absolute path - ex.
# with open("C:\\Users\\eyal1\\PycharmProjects\\grades.txt") as file:
#     print(file.read())

# relative path - ex.
# with open("../../grades.txt") as file:
#     print(file.read())
# note: ../ -> 1 folder "up"
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


def colorize(text, color):
    if type(text) is not str:
        raise TypeError("Text must be a string. (don't be an invalid)")
    else:
        print(f"Printed {text} in {color}")


colorize(3, "red")
