from model import MoveDirection

class OptionsParser:
    @staticmethod
    def parse(args):
        valid_directions = {'f', 'b', 'l', 'r'}
        directions = []
        for arg in args:
            if arg in valid_directions:
                if arg == 'f':
                    directions.append(MoveDirection.FORWARD)
                elif arg == 'b':
                    directions.append(MoveDirection.BACKWARD)
                elif arg == 'l':
                    directions.append(MoveDirection.LEFT)
                elif arg == 'r':
                    directions.append(MoveDirection.RIGHT)
        return directions

