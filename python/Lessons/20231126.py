# parrot = "Norwegian"

# print(parrot[:6] + parrot[6:])
# print(parrot[:])

# letters = "abcdefghijklmnopqrstuvwxyz"
# x = parrot[99]
# print(x)
# print(parrot[-4:2])
# print(parrot[-4:-2])  # gi
# print(parrot[-4:12])
# parrot = "Norwegian"
# print(parrot[-14:-8])

# parrot = "Norwegian Blue"
# print(parrot[0:6:2])  # Nre
# print(parrot[0:6:3])  # Nw
# print(parrot[6:0:-2]) # ier

# number = "9,223,372,036,854,775,807"
# print(number[1::4])
# number = "9,223;372:036 854,775;807"
# separators = number[1::4]
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])
#  list comprehension

# letters = "abcdefghijklmnopqrstuvwxyz"
# backwards = letters[::-1]
# print(backwards)
# idiom

# String Formatting (uses string replacement fields)
# {} - string interpolation
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))

