'''
ENCAPSULATION - הכמסה
'''

# a = 12
# b = 4
# print(a + b)
# print(a.__add__(b))


class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
# print(kenwood.make)
# print(kenwood.price)

kenwood.price = 12.75
# print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.on)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price,
                                        hamilton.make, hamilton.price))

# data attributes
# {} => placeholders

