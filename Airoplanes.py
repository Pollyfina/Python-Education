from random import randint
from random import choice
from math import sqrt


airlines = ['S7', 'Air Baltic', 'Aeroflot', 'Delta airlines']
list_of_planes = list()
dict_of_distance = {}


class Planes(object):
    def __init__(self, x, y, company):
        self.x = x
        self.y = y
        self.company = company
    def calculate_distance(self, another_plane):
        if self.x >= another_plane.x and self.y >= another_plane.y:
            x = self.x - another_plane.x
            y = self.y - another_plane.y
            distance = sqrt(x^2 + y^2)
        elif self.x >= another_plane.x and self.y < another_plane.y:
            x = self.x - another_plane.x
            y = another_plane.y - self.y
            distance = sqrt(x^2 + y^2)
        elif self.x < another_plane.x and self.y >= another_plane.y:
            x = another_plane.x - self.x
            y = self.y - another_plane.y
            distance = sqrt(x^2 + y^2)
        else:
            x = another_plane.x - self.x
            y = another_plane.y - self.y
            distance = sqrt(x^2 + y^2)


def making_planes(number_of_planes=100):
    for plane in range(number_of_planes):
        x = randint(1, 11)
        y = randint(1, 11)
        company = choice(airlines)
        plane = Planes(x, y, company)
        list_of_planes.append(plane)


def find_the_nearest_plane():
    the_plane = choice(list_of_planes)
    list_of_planes.remove(the_plane)
    for another_plane in list_of_planes:
        the_plane.calculate_distance(another_plane)
        dict_of_distance[another_plane] = the_plane.calculate_distance(another_plane)
    return min(dict_of_distance)
    

making_planes(10)
print(list_of_planes)
print(find_the_nearest_plane())