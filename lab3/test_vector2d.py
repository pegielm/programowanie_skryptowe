from model import Vector2d

vector1 = Vector2d(1, 2)
vector2 = Vector2d(3, 4)

def test_get_x():
    assert vector1.get_x() == 1
    assert vector2.get_x() == 3
def test_get_y():
    assert vector1.get_y() == 2
    assert vector2.get_y() == 4
def test_str():
    assert str(vector1) == "(1,2)"
    assert str(vector2) == "(3,4)"
def test_precedes():
    assert vector1.precedes(vector2) == True
    assert vector2.precedes(vector1) == False
def test_follows():
    assert vector1.follows(vector2) == False
    assert vector2.follows(vector1) == True
def test_add():
    assert vector1.add(vector2) == Vector2d(4,6)
    assert vector2.add(vector1) == Vector2d(4,6)
def test_subtract():
    assert vector1.subtract(vector2) == Vector2d(-2,-2)
    assert vector2.subtract(vector1) == Vector2d(2,2)
def test_upperRight():
    assert vector1.upperRight(vector2) == Vector2d(3,4)
    assert vector2.upperRight(vector1) == Vector2d(3,4)
def test_lowerLeft():
    assert vector1.lowerLeft(vector2) == Vector2d(1,2)
    assert vector2.lowerLeft(vector1) == Vector2d(1,2)
def test_opposite():
    assert vector1.opposite() == Vector2d(-1,-2)
    assert vector2.opposite() == Vector2d(-3,-4)
def test_eq():
    assert vector1 == Vector2d(1,2)
    assert vector2 == Vector2d(3,4)
    assert vector1 != vector2
    assert vector2 != vector1

