from controller import OptionsParser
from model import MoveDirection
moves = OptionsParser.parse(['f', 'b', 'l', 'r'])
moves2 = OptionsParser.parse(['f', '1', 'x', 'd', 'fb', 'b', 'l', 'r'])
def test_parse_no_errors():
    assert moves == [MoveDirection.FORWARD, MoveDirection.BACKWARD, MoveDirection.LEFT, MoveDirection.RIGHT]
def test_parse_errors():
    assert moves2 == [MoveDirection.FORWARD, MoveDirection.BACKWARD, MoveDirection.LEFT, MoveDirection.RIGHT]