class PositionAlreadyOccupiedError(Exception):
    def __init__(self, position):
        super().__init__(f"Position {position} is already occupied.")