from model.interface import IMoveValidator, IWorldMap
from model.core import Vector2d, MoveDirection
from model.animal import Animal
from view import MapVisualizer

class WorldMap(IWorldMap,IMoveValidator):
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
    def canMoveTo(self,position):
        if type(position) != Vector2d:
            raise TypeError("Position must be Vector2d")
        if position in self.animals.keys():
            return False
        return True

class RectangularMap(WorldMap):
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
        if position.x < 0 or position.x > self.__width or position.y < 0 or position.y > self.__height:
            return False
        return super().canMoveTo(position)
        
    def __str__(self):
        map_vizualizer = MapVisualizer(self)
        return map_vizualizer.draw(Vector2d(0, 0), Vector2d(self.__width, self.__height))


class InfiniteMap(WorldMap):
    def __init__(self):
        self.animals: dict[Vector2d, Animal] = {}
    
    def __str__(self):
        max_x = 0
        max_y = 0
        min_x = 0
        min_y = 0
        for animal in self.animals.values():
            if animal.position.x < min_x:
                min_x = animal.position.x
            if animal.position.x > max_x:
                max_x = animal.position.x
            if animal.position.y < min_y:
                min_y = animal.position.y
            if animal.position.y > max_y:
                max_y = animal.position.y
        map_vizualizer = MapVisualizer(self)
        return map_vizualizer.draw(Vector2d(min_x, min_y), Vector2d(max_x, max_y))

