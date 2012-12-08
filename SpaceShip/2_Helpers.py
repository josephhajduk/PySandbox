import math

# helper functions to handle transformations

def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def scale(p,c):
    return [p[0]*c,p[1]*c]

def add_vec(a,b):
    return [a[0]+b[0],a[1]+b[1]]

