#!/usr/bin/env python3
import sys
from model.core import Vector2d, MoveDirection
from model.interface import IWorldMap
from model.map import RectangularMap   
from controller import Simulation, OptionsParser
directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:])
positions: list[Vector2d] = [Vector2d(0,0),Vector2d(2, 2), Vector2d(3, 3), Vector2d(1, 1), Vector2d(9,9)]
# Poprzednio
# simulation: Simulation = Simulation(directions, positions)
# simulation.run()
# Obecnie
map = RectangularMap(10, 10)
simulation: Simulation = Simulation(directions, positions, map)
simulation.run()