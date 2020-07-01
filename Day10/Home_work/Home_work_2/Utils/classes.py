from abc import ABC, abstractmethod


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def get_xy(self):
        return {"x": self.__x, "y": self.__y}


class Figure(ABC):
    @abstractmethod
    def get_perimeter(self):
        print("Method not defined")

    @abstractmethod
    def get_area(self):
        print("Method not defined")


class Circle(Figure):
    import math
    def __init__(self, center, radius):
        self.__center = center.get_xy
        self.__radius = radius

    @property
    def get_perimeter(self):
        return round(2 * self.math.pi * self.__radius, 3)

    @property
    def get_area(self):
        return round(self.math.pi * (self.__radius ** 2), 3)

    def __str__(self):
        return f"Circle (O = {self.__center}, R = {self.__radius})"


class Triangle(Figure):
    import math
    def __init__(self, point_a, point_b, point_c):
        self.__point_a = point_a.get_xy
        self.__point_b = point_b.get_xy
        self.__point_c = point_c.get_xy

    @property
    def get_side(self):
        ab = self.math.sqrt(
            (self.__point_a["x"] - self.__point_b["x"]) ** 2 + (self.__point_a["y"] - self.__point_b["y"]) ** 2)
        bc = self.math.sqrt(
            (self.__point_b["x"] - self.__point_c["x"]) ** 2 + (self.__point_b["y"] - self.__point_c["y"]) ** 2)
        ca = self.math.sqrt(
            (self.__point_c["x"] - self.__point_a["x"]) ** 2 + (self.__point_c["y"] - self.__point_a["y"]) ** 2)
        return {"ab": ab, "bc": bc, "ca": ca}

    @property
    def get_perimeter(self):
        side = self.get_side
        return round((side["ab"] + side["bc"] + side["ca"]) / 2, 3)

    @property
    def get_area(self):
        side = self.get_side
        p = self.get_perimeter
        h = (2 * self.math.sqrt(p * (p - side["ca"]) * (p - side["ab"]) * (p - side["bc"]))) / side["bc"]
        return round((side["bc"] * h) / 2, 3)

    def __str__(self):
        return f"Triangle (A = {self.__point_a}, B = {self.__point_b}, C = {self.__point_c})"


class Square(Figure):
    import math
    def __init__(self, point_a, point_b):
        self.__point_a = point_a.get_xy
        self.__point_b = point_b.get_xy

    @property
    def get_diagonal(self):
        diagonal = self.math.sqrt(
            (self.__point_a["x"] - self.__point_b["x"]) ** 2 + (self.__point_a["y"] - self.__point_b["y"]) ** 2)
        return diagonal

    @property
    def get_perimeter(self):
        diagonal = self.get_diagonal
        return round(diagonal * self.math.sqrt(2) * 2, 3)

    @property
    def get_area(self):
        diagonal = self.get_diagonal
        return round((diagonal * self.math.sqrt(2) / 2) ** 2, 3)

    def __str__(self):
        return f"Square (A = {self.__point_a}, C = {self.__point_b})"
