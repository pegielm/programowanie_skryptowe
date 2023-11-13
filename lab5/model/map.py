from model.interface import IMoveValidator, IWorldMap
from model.core import Vector2d, MoveDirection
from model.animal import Animal

class RectangularMap(IWorldMap, IMoveValidator):
    def __init__(self,width,height):
        self.__width = width
        self.__height = height
        self.animals: dict[Vector2d, Animal] = {}
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    def canMoveTo(self,position):
        if type(position) != Vector2d:
            raise TypeError("Position must be Vector2d")
        if position.x < 0 or position.x > self.__width or position.y < 0 or position.y > self.__height:
            return False
        if position in self.animals.keys():
            return False
        return True
    def place(self,animal):
        if type(animal) != Animal:
            raise TypeError("Animal must be Animal")
        if self.canMoveTo(animal.position):
            self.animals[animal.position] = animal
            return True
        else:
            return False
    def isOccupied(self,position):
        if type(position) != Vector2d:
            raise TypeError("Position must be Vector2d")
        if position in self.animals.keys():
            return True
        else:
            return False
    def move(self,animal,direction):
        if type(animal) != Animal:
            raise TypeError("Animal must be Animal")
        if type(direction) != MoveDirection:
            raise TypeError("Direction must be MoveDirection")
        if animal.position in self.animals.keys():
            del self.animals[animal.position]
        animal.move(direction,self)
        self.animals[animal.position] = animal
    def objectAt(self, position: Vector2d):
        if type(position) != Vector2d:
            raise TypeError("Position must be Vector2d")
        if position in self.animals.keys():
            return self.animals[position]
        else:
            return None
    
    