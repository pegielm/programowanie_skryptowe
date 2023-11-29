<<<<<<< HEAD
from operator import index
from time import sleep
from model.core import *
from model.animal import *
from model.interface import *
from model.map import *
from view import *
from model.errors import *

class OptionsParser:
    @staticmethod
    def parse(args):
        '''directions = []
        for arg in args:
            try:
                if arg == 'f':
                    arg=1
                elif arg == 'r':
                    arg=2
                elif arg == 'b':
                    arg=3
                elif arg == 'l':
                    arg=4
                directions.append(MoveDirection(arg))
            except ValueError:
                raise ValueError(f"Wrong argument: {arg}")
        return directions'''
        moves = ['f','r','b','l']
        directions = list(filter(lambda x: x in moves, args))
        return [MoveDirection(moves.index(x)+1) for x in directions]

class Simulation:
    animals = []
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d],map ) -> None:
        self.__directions = directions
        self.__positions = positions
        self.__map = map
        for i in range(len(self.__positions)):
            try:
                self.__map.place(Animal(self.__positions[i]))
            except PositionAlreadyOccupiedError as e:
                print(e)
                exit(1)
            self.animals.append(Animal(self.__positions[i]))
    
    def run(self):
        print(self.__map)
        for i in range(len(self.__directions)):
            self.__map.move(self.animals[i%len(self.animals)],self.__directions[i])
            sleep(0.5)
            print(self.__map)  
=======
from operator import index
from time import sleep
from model.core import *
from model.animal import *
from model.interface import *
from model.map import *
from view import *
from model.errors import *

class OptionsParser:
    @staticmethod
    def parse(args):
        '''directions = []
        for arg in args:
            try:
                if arg == 'f':
                    arg=1
                elif arg == 'r':
                    arg=2
                elif arg == 'b':
                    arg=3
                elif arg == 'l':
                    arg=4
                directions.append(MoveDirection(arg))
            except ValueError:
                raise ValueError(f"Wrong argument: {arg}")
        return directions'''
        moves = ['f','r','b','l']
        directions = list(filter(lambda x: x in moves, args))
        return [MoveDirection(moves.index(x)+1) for x in directions]

class Simulation:
    animals = []
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d],map ) -> None:
        self.__directions = directions
        self.__positions = positions
        self.__map = map
        for i in range(len(self.__positions)):
            try:
                self.__map.place(Animal(self.__positions[i]))
            except PositionAlreadyOccupiedError as e:
                print(e)
                exit(1)
            self.animals.append(Animal(self.__positions[i]))
    
    def run(self):
        print(self.__map)
        for i in range(len(self.__directions)):
            self.__map.move(self.animals[i%len(self.animals)],self.__directions[i])
            sleep(0.5)
            print(self.__map)  
>>>>>>> 5477586dc342db89ac9559ff29ef2d4846b8911e
