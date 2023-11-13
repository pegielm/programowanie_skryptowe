from operator import index
from time import sleep
from model.core import *
from model.animal import *
from model.interface import *
from model.map import *
from view import *

class OptionsParser:
    @staticmethod
    def parse(args):
        directions = []
        for arg in args:
            try:
                directions.append(MoveDirection(arg))
            except ValueError:
                continue
        return directions
class Simulation:
    animals = []
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d],map: RectangularMap ) -> None:
        self.__directions = directions
        self.__positions = positions
        self.__map = map
        for i in range(len(self.__positions)):
            self.__map.place(Animal(self.__positions[i]))
            self.animals.append(Animal(self.__positions[i]))
        
    
    def run(self):
        map_vizualizer = MapVisualizer(self.__map)
        print(map_vizualizer.draw(Vector2d(0, 0), Vector2d(self.__map.width, self.__map.height)))
        for i in range(len(self.__directions)):
            self.__map.move(self.animals[i%len(self.animals)],self.__directions[i])
            sleep(1)
            print(map_vizualizer.draw(Vector2d(0, 0), Vector2d(self.__map.width, self.__map.height)))
                
