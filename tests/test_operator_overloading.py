import pytest

from operator_overloading.complex_number import ComplexNumber
from operator_overloading.person import Person
from operator_overloading.vector import Vector
from operator_overloading.circle import Circle
from operator_overloading.point import Point
from operator_overloading.matrix import Matrix


def test_complex_add_and_sub():
    z1 = ComplexNumber(3, 2)
    z2 = ComplexNumber(1, 7)
    assert z1 + z2 == ComplexNumber(4, 9)
    assert z1 - z2 == ComplexNumber(2, -5)


def test_person_older():
    alice = Person("Alice", 25, "female")
    bob = Person("Bob", 30, "male")
    assert bob > alice
    assert not alice > bob


def test_vector_dot_product():
    assert Vector(1, 2, 3) * Vector(4, 5, 6) == 32


def test_circle_comparisons():
    small, big = Circle(2), Circle(5)
    assert small < big
    assert big > small
    assert small <= big
    assert big >= small
    assert small != big
    assert Circle(3) == Circle(3)


def test_point_distance_comparisons():
    assert Point(1, 1) < Point(3, 4)
    assert Point(3, 4) == Point(5, 0)  # same distance (5)
    assert Point(3, 4) >= Point(1, 1)


def test_matrix_multiplication():
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    assert a * b == Matrix([[19, 22], [43, 50]])


def test_matrix_wrong_size():
    a = Matrix([[1, 2, 3]])   # 1 x 3
    b = Matrix([[1, 2]])      # 1 x 2
    with pytest.raises(ValueError):
        a * b
