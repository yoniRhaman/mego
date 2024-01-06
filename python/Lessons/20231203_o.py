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

# lists
# dictionaries
# tuples
# sets

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

with open("my_fi.txt", mode="r+") as file:
    file.write("I am Groot!")
    # the cursor moves to the end of the string!!!

    # that is why the following code printed "nothing"
    # contents = file.read()
    # print(contents)

with open("my_fi.txt") as file:
    contents = file.read()
    print(contents)
