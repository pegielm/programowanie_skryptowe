#!/usr/bin/env python3
import sys
from model.core import Vector2d, MoveDirection
from model.interface import IWorldMap
from model.map import *
from controller import Simulation, OptionsParser
directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:])
positions: list[Vector2d] = [Vector2d(4, 3), Vector2d(5, 5), Vector2d(7,7)]
# Poprzednio
# simulation: Simulation = Simulation(directions, positions)
# simulation.run()
# Obecnie
map = InfiniteMap()
simulation: Simulation = Simulation(directions, positions, map)
simulation.run()