from model.core import MapDirection, MoveDirection, Vector2d
from model.interface import IMoveValidator, IWorldMap
MAP_WIDTH = 4
MAP_HEIGHT = 4

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
        return f'{self.__orientation}'
    def __repr__(self) -> str:
        return f'{self.__orientation}'
    def isAt(self,position):
        if type(position) != Vector2d:
            raise TypeError("Position must be Vector2d")
        if position == self.__position:
            return True
        else:
            return False
    def move(self, direction: MoveDirection, validator: IMoveValidator):
        if type(direction) != MoveDirection:
            raise TypeError("Direction must be MoveDirection")
        if isinstance(validator, IMoveValidator) == False:
            raise TypeError("Validator must be IMoveValidator")
        if direction == MoveDirection.FORWARD:
            if validator.canMoveTo(self.__position + self.__orientation.toUnitVector()):
                self.__position += self.__orientation.toUnitVector()
        elif direction == MoveDirection.BACKWARD:
            if validator.canMoveTo(self.__position - self.__orientation.toUnitVector()):
                self.__position -= self.__orientation.toUnitVector()
        elif direction == MoveDirection.LEFT:
            self.__orientation = self.__orientation.previous()
        elif direction == MoveDirection.RIGHT:
            self.__orientation = self.__orientation.next()
        else:
            raise ValueError("Wrong direction")
        