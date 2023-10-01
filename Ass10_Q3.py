#Display all the modules, variables and functions that are defined under module math
import math

# Get a list of all attributes (modules, variables, functions) of the math module
math_attributes = dir(math)

for attribute in math_attributes:
    print(attribute)