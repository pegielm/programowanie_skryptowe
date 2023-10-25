from enum import Enum

class MoveDirection(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4

class Vector2d:
    def __init__(self, xi, yi):
        self.__x = xi
        self.__y = yi
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f'({self.__x},{self.__y})'

    def precedes(self, other):
        return self.__x <= other.x and self.__y <= other.y

    def follows(self, other):
        return self.__x >= other.x and self.__y >= other.y

    def add(self, other):
        return Vector2d(self.__x + other.x, self.__y + other.y)

    def subtract(self, other):
        return Vector2d(self.__x - other.x, self.__y - other.y)

    def upperRight(self, other):
        return Vector2d(max(self.__x, other.x), max(self.__y, other.y))

    def lowerLeft(self, other):
        return Vector2d(min(self.__x, other.x), min(self.__y, other.y))

    def opposite(self):
        return Vector2d(-self.__x, -self.__y)

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

