from model import *
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
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d]) -> None:
        self.__directions = directions
        self.__positions = positions
        for i in range(len(self.__positions)):
            self.animals.append(Animal(self.__positions[i]))
    
    def run(self) -> None:
        for i in range(len(self.__directions)):
            self.animals[i % len(self.animals)].move(self.__directions[i])
            print(self.animals[i % len(self.animals)])
