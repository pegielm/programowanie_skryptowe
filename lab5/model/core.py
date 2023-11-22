from enum import Enum
class MoveDirection(Enum):
    FORWARD = 'f'
    BACKWARD = 'b'
    LEFT = 'l'
    RIGHT = 'r'

class MapDirection(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    def __str__(self) -> str:
        if self == MapDirection.NORTH:
            return "↑"
        elif self == MapDirection.SOUTH:
            return "↓"
        elif self == MapDirection.WEST:
            return "←"
        elif self == MapDirection.EAST:
            return "→"
    def next(self):
        if self == MapDirection.NORTH:
            return MapDirection.EAST
        elif self == MapDirection.SOUTH:
            return MapDirection.WEST
        elif self == MapDirection.WEST:
            return MapDirection.NORTH
        elif self == MapDirection.EAST:
            return MapDirection.SOUTH
    def previous(self):
        if self == MapDirection.NORTH:
            return MapDirection.WEST
        elif self == MapDirection.SOUTH:
            return MapDirection.EAST
        elif self == MapDirection.WEST:
            return MapDirection.SOUTH
        elif self == MapDirection.EAST:
            return MapDirection.NORTH
    def toUnitVector(self):
        if self == MapDirection.NORTH:
            return Vector2d(0,1)
        elif self == MapDirection.SOUTH:
            return Vector2d(0,-1)
        elif self == MapDirection.WEST:
            return Vector2d(-1,0)
        elif self == MapDirection.EAST:
            return Vector2d(1,0)
    
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
    
    def __hash__(self) -> int:
        return hash((self.__x, self.__y))
    def __add__(self, other):
        return Vector2d(self.__x + other.x, self.__y + other.y)
    def __sub__(self, other):
        return Vector2d(self.__x - other.x, self.__y - other.y)
    



