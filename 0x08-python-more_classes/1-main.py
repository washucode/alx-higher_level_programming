#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

myrectangle = Rectangle(2, 4)
print("{} - {}").format(myrectangle.width, myrectangle.height)

myrectangle.height = 10 
print("{} - {}").format(myrectangle.width, myrectangle.height)
