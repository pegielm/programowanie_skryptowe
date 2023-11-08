from model import MoveDirection
from controller import OptionsParser
import sys
print("start")
def run():
    
    moves_descriptions = {
        MoveDirection.FORWARD: 'przód',
        MoveDirection.BACKWARD: 'tył',
        MoveDirection.RIGHT: 'prawo',
        MoveDirection.LEFT: 'lewo'
    }

    moves = OptionsParser.parse(sys.argv[1:])
    descriptions = [moves_descriptions[move] for move in moves]
    for x in descriptions: 
        print(x)
run()

print("stop")