from classes import *
from random import randrange

quantity_points = 10
quantity_figures = 10
points = []
figures = []

for i in range(quantity_points):
    points.append(Point(randrange(-100, 100), randrange(-100, 100)))

for i in range(len(points)):
    print(f"Point {i}:{points[i].get_xy}")

for i in range(quantity_figures):
    type_figure = randrange(0,3)
    if type_figure == 0:
        figures.append(Circle(points[randrange(0,quantity_points)],randrange(0,100)))
    elif type_figure ==1:
        figures.append(Triangle(points[randrange(0,quantity_points)],points[randrange(0,quantity_points)],points[randrange(0,quantity_points)]))
    elif type_figure ==2:
        figures.append(Square(points[randrange(0,quantity_points)],points[randrange(0,quantity_points)]))

for i in range(len(figures)):
    print(f"Figure {i}: {figures[i]}")

area = 0
perimeter = 0

for i in figures:
    perimeter += i.get_perimeter
    area += i.get_area

print(f"Perimeter = {perimeter}")
print(f"Area = {area}")



