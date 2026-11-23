"""Problem 6 - 2D point: compare points by their distance from the origin."""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        # Euclidean distance: sqrt(x^2 + y^2)
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # All comparisons use the distance from the origin
    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __gt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def __eq__(self, other):
        # Note: two different points can be "equal" if they are at the same distance,
        # e.g. (3, 4) and (5, 0) are both at distance 5.
        return self.distance_from_origin() == other.distance_from_origin()

    def __ne__(self, other):
        return self.distance_from_origin() != other.distance_from_origin()

    def __le__(self, other):
        return self.distance_from_origin() <= other.distance_from_origin()

    def __ge__(self, other):
        return self.distance_from_origin() >= other.distance_from_origin()

    def __str__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    a = Point(1, 1)  # distance ~1.41
    b = Point(3, 4)  # distance 5
    c = Point(5, 0)  # distance 5
    print(a, "<", b, ":", a < b)    # True
    print(b, "==", c, ":", b == c)  # True (same distance)
    print(b, ">=", a, ":", b >= a)  # True
