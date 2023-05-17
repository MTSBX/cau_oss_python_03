import math
class line:
    def __init__(self, __length=0):
        self.__length = __length

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

def area_square(length):
    return length ** 2

def area_circle(length):
    return math.pi * (length ** 2)

def area_regular_triangle(length):
    return (math.sqrt(3) / 4) * (length** 2)