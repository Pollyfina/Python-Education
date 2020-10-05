from random import randint
from random import choice
from math import sin
from math import radians
from tkinter import *


tk = Tk()
map_of_planes = Canvas(tk, width=500, height=500)
map_of_planes.pack()


airlines = ['S7', 'Air Baltic', 'Aeroflot', 'Delta airlines']
list_of_planes = list()
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'magenta', 'pink', 'lime']


class Planes(object):
    def __init__(self, x, y, company, speed, direction, color):
        self.x = x
        self.y = y
        self.company = company
        self.speed = speed
        self.direction = direction
        self.color = color 
    def find_angle(self):
        if self.direction >= 1 and self.direction <= 90:
            z = 90 - self.direction
            w = 90 - z
        elif self.direction > 90 and self.direction <= 180:
            w = 180 - self.direction
            z = 90 - w
        elif self.direction > 180 and self.direction <=270:
            z = 270 - self.direction
            w = 90 - z
        else:
            w = 360 - self.direction
            z = 90 - w
        z = radians(z)
        w = radians(w)
        sin_z = sin(z)
        sin_w = sin(w)
        catheti_x = self.speed * sin_w
        catheti_y = self.speed * sin_z
        if self.direction < 90 and self.direction > 0:
            self.x = self.x + catheti_x
            self.y = self.y + catheti_y
        elif self.direction >= 90 and self.direction < 180:
            self.x = self.x + catheti_x
            self.y = self.y - catheti_y
        elif self.direction >= 180 and self.direction < 270:
            self.x = self.x - catheti_x
            self.y = self.y + catheti_y
        else:
            self.x = self.x - catheti_x
            self.y = self.y - catheti_y
    def change_of_planes(self):
        if self.direction < 16 and self.speed < 301:
            self.direction = self.direction + 15
            self.speed = self.speed + 300
        elif self.direction >= 16 and self.speed < 301:
            change_d = choice([-15, 15])
            self.direction = self.direction + change_d
            self.speed = self.speed + 300
        elif self.direction < 16 and self.speed >= 301:
            self.direction = self.direction + 15
            change_s = choice([-300, 300])
            self.speed = self.speed + change_s
        else:
            change_d = choice([-15, 15])
            self.direction = self.direction + change_d
            change_s = choice([-300, 300])
            self.speed = self.speed + change_s
    def draw(self, x1, x2,):
        k = 10 #масштаб "карты"
        x1 = round(x1/k)
        x2 = round(self.x/k)
        y1 = round(y1/k)
        y2 = round(self.y/k)
        map_of_planes.create_line(x1, self.x , y1, self.y, fill='self.color')


def making_planes(number_of_planes=20):
    for plane in range(number_of_planes):
        x = randint(1, 5000)
        y = randint(1, 5000)
        company = choice(airlines)
        speed = randint(100,1001)
        direction = randint(0,361)
        color = choice(colors)
        plane = Planes(x, y, company, speed, direction, color)
        list_of_planes.append(plane)


def playing(move):
    for i in range(move):
            for a_plane in list_of_planes:
                x1 = a_plane.x
                y1 = a_plane.y
                a_plane.change_of_planes()
                a_plane.find_angle()
                a_plane.draw(x1, x2,)
                if a_plane.x > 5000 or a_plane.x < 0 or a_plane.y < 0 or a_plane.y > 5000:
                    print(a_plane.x, a_plane.y)
                    list_of_planes.remove(a_plane)
                else:
                    pass


making_planes()
playing(10)