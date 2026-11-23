"""Problem 2 - Person: overload > to compare people by age."""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        # p1 > p2 is True if p1 is older than p2
        return self.age > other.age

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


if __name__ == "__main__":
    alice = Person("Alice", 25, "female")
    bob = Person("Bob", 30, "male")
    print(alice, ">", bob, "?", alice > bob)  # False
    print(bob, ">", alice, "?", bob > alice)  # True
