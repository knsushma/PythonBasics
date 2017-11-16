"""This is how the document must be done, within 3 double quotes"""
#import math
from math import pi as pii
# pii and sine are alias for pi and sin functions from the module math
# Identifiers are case sensitive

print("Lets find area of circle")
radius = float(input("enter the radius of circle"))
print(radius)
area = pii * (radius ** 2)
print("Area of circle:", area)

# **************************************************

# using functions
def compute_area(radius):
    return pii * radius * radius


try:
    area = compute_area(radius)
    print("Area of circle inside try:" , area)
    print("Area: {}".format(area)) # string formatting, {} -> place holder, {:fmt-str} -> format for string_formatting
    print("Radius : {}\n Area: {:.3f}".format(radius, area))
except Exception as e:
    print(e)