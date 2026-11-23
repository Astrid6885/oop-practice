"""Problem 5 - Circle: overload the 6 comparison operators (compare by radius)."""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):  # <
        return self.radius < other.radius

    def __gt__(self, other):  # >
        return self.radius > other.radius

    def __eq__(self, other):  # ==
        return self.radius == other.radius

    def __ne__(self, other):  # !=
        return self.radius != other.radius

    def __ge__(self, other):  # >=
        return self.radius >= other.radius

    def __le__(self, other):  # <=
        return self.radius <= other.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


if __name__ == "__main__":
    small = Circle(2)
    big = Circle(5)
    print("small < big  :", small < big)    # True
    print("small > big  :", small > big)    # False
    print("small == big :", small == big)   # False
    print("small != big :", small != big)   # True
    print("small >= big :", small >= big)   # False
    print("small <= big :", small <= big)   # True
