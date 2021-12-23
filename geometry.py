from math import pi, sqrt

def area_of_circle(radius):
    return pi*(radius ** 2)
def get_hypotenuse(a,b):
    c_sqr= a**2 + b**2
    c=sqrt(c_sqr)
    return c
get_hypotenuse(3,4)
