# Basic
"""
print("Hello, world!")
"""


# input example
"""
name = input("Name: ")
print("Hello, " + name)
"""

#calc example - Error model with type error
"""
num = input("Number: ")
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")
"""
    
#calc example
"""
num = int(input("Number: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")
"""

#list example
"""
# This is a Python comment
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:
names.append("Draco")
# Sort the list:
names.sort()
# Print the new list:
print(names)
"""

#set data example
"""
# Create an empty set:
s = set()

# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set:
print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements.")
"""


# dictionary example
"""
# Define a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Print out Harry's house
print(houses["Harry"])
# Adding values to a dictionary:
houses["Hermione"] = "Gryffindor"
# Print out Hermione's House:
print(houses["Hermione"])

#for loop
for i in [0, 1, 2, 3, 4, 5]:
    print(i)


#range
for i in range(6):
    print(i)

"""

#list technique
"""
# Create a list:
names = ["Harry", "Ron", "Hermione"]

# Print each name:
for name in names:
    print(name)

name = "Harry"
for char in name:
    print(char)
"""

#function example
"""
def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")
"""


# module example
"""
from function import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")
"""

# class example
"""
class Point():
    # A method defining how to create a point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)
"""

# debug comment example

def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()


# sort with multiple lists - Error
"""
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort()

print(people)
"""


# sort with multiple lists - using lambda make multiple lists as one list
"""
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)
"""

# exception case - simple calculation
"""
x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")
"""

# exception case - ZeroDivisionError
"""
import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")
"""

# exception case - ZeroDivisionError and ValueError

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")