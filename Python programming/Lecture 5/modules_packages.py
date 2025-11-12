from circumference import circumference


# Module Alias
import math as m
import numpy as np



def calculate_circle_area(radius):
    return m.pi * (radius ** 2)

def create_numpy_array(data):
    return np.array(data)

def calculate_circle_circumference(radius):
    return circumference(radius)

calculate_circle_area(5)
create_numpy_array([1, 2, 3, 4, 5])
circumference(5)
