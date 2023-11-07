from enum import Enum
MAP_WIDTH = 4
MAP_HEIGHT = 4
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
    

class Animal:
    def __init__(self,position):
        if type(position) != Vector2d:
            raise TypeError("Position must be Vector2d")
        self.__position = position
        self.__orientation = MapDirection.NORTH
    @property
    def position(self):
        return self.__position
    @property
    def orientation(self) -> MapDirection:
        return self.__orientation
    def __str__(self) -> str:
        return f'{self.__position} {self.__orientation}'
    def isAt(self,position):
        if type(position) != Vector2d:
            raise TypeError("Position must be Vector2d")
        if position == self.__position:
            return True
        else:
            return False
    def move(self,orientation: MoveDirection) -> None:
        if type(orientation) != MoveDirection:
            raise TypeError("Direction must be MoveDirection")
        if orientation == MoveDirection.FORWARD:
            if self.__position.add(self.__orientation.toUnitVector()).x > MAP_WIDTH or self.__position.add(self.__orientation.toUnitVector()).y > MAP_HEIGHT or self.__position.add(self.__orientation.toUnitVector()).x < 0 or self.__position.add(self.__orientation.toUnitVector()).y < 0:
                return
            self.__position = self.__position.add(self.__orientation.toUnitVector())
        elif orientation == MoveDirection.BACKWARD:
            if self.__position.subtract(self.__orientation.toUnitVector()).x > MAP_WIDTH or self.__position.subtract(self.__orientation.toUnitVector()).y > MAP_HEIGHT or self.__position.subtract(self.__orientation.toUnitVector()).x < 0 or self.__position.subtract(self.__orientation.toUnitVector()).y < 0:
                return
            self.__position = self.__position.subtract(self.__orientation.toUnitVector())
        elif orientation == MoveDirection.LEFT:
            self.__orientation = self.__orientation.previous()
        elif orientation == MoveDirection.RIGHT:
            self.__orientation = self.__orientation.next()
        else:
            raise ValueError("Wrong orientation")

if __name__ == "__main__":
    animal = Animal(Vector2d(2,2))
    print(animal)
    animal.move(MoveDirection.FORWARD)
    print(animal)
    animal.move(MoveDirection.FORWARD)
    print(animal)
    animal.move(MoveDirection.FORWARD)
    print(animal)


