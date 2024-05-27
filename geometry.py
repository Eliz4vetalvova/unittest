import math

def volume_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * radius**3

def volume_cube(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side**3

def volume_cylinder(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    return math.pi * radius**2 * height