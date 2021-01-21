class Road:
    def __init__(self, _distance, _width):
        self._distance = _distance
        self._width = _width

    def mass(self):
        return (self._distance * self._width * self._weight * self._depth)/1000

class count(Road):
    def __init__(self, _distance, _width, _weight, _depth):
        super().__init__(_distance, _width)
        self._weight = _weight
        self._depth = _depth

data = count(20, 5000, 25, 5)

print(data.mass(), ' тонн')