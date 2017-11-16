"""a sample script to demo io"""
from math import pi, floor, ceil


def compute_area(given_radius):  # function definition
    """
    compute_area, its does the computation for the given ip
    :param given_radius:
    :return:
    """
    return pi * (given_radius ** 2)


try:
    radius = float(input('enter the radius :'))
    area = compute_area(radius)  # calling
    print("radius : {}\narea : {:.3f}".format(radius, area))
except ValueError as err:
    print(err)
