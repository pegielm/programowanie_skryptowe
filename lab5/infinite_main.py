#!/usr/bin/env python3
import sys
from model.core import Vector2d, MoveDirection
from model.interface import IWorldMap
from model.map import *
from controller import Simulation, OptionsParser
'''
infinite_main.py l f r r f f f r f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
'''
directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:])
positions: list[Vector2d] = [Vector2d(1, 1), Vector2d(1,2), Vector2d(2,1),Vector2d(2,2)]
# Poprzednio
# simulation: Simulation = Simulation(directions, positions)
# simulation.run()
# Obecnie
map = InfiniteMap()
simulation: Simulation = Simulation(directions, positions, map)
simulation.run()