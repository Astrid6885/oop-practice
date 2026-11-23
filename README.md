# OOP Practice (Python)

Beginner solutions to the OOP mini practice of the OOP course (AIDAMS 2A).

## Structure

```
oop-practice/
├── operator_overloading/
│   ├── complex_number.py   # Problem 1 - + and - for complex numbers
│   ├── person.py           # Problem 2 - > compares people by age
│   ├── vector.py           # Problem 4 - * gives the dot product
│   ├── circle.py           # Problem 5 - the 6 comparison operators (by radius)
│   ├── point.py            # Problem 6 - compare points by distance from the origin
│   └── matrix.py           # Problem 7 - * multiplies two matrices
├── inheritance/
│   ├── vehicle.py          # Problem 1 - Vehicle -> Car, Bicycle
│   ├── person.py           # Problem 2 - Person -> Student, Employee
│   └── bank_account.py     # Problem 3 - BankAccount -> SavingsAccount
└── tests/                  # pytest tests for every problem
```

(There is no Problem 3 in the "Operator Overloading" section of the exercise sheet.)

## Run an example

Each file has a small demo at the bottom (`if __name__ == "__main__":`).
From the root of the repo:

```bash
python -m operator_overloading.vector
python -m inheritance.bank_account
```

## Run the tests

```bash
pip install pytest
python -m pytest
```

## Key ideas

- **Operator overloading**: Python calls special ("dunder") methods behind the scenes.
  `a + b` calls `a.__add__(b)`, `a > b` calls `a.__gt__(b)`, `a * b` calls `a.__mul__(b)`.

  | Operator | Method   | Operator | Method   |
  |----------|----------|----------|----------|
  | `+`      | `__add__`| `<`      | `__lt__` |
  | `-`      | `__sub__`| `<=`     | `__le__` |
  | `*`      | `__mul__`| `>`      | `__gt__` |
  | `==`     | `__eq__` | `>=`     | `__ge__` |
  | `!=`     | `__ne__` |          |          |

- **Inheritance**: a child class gets all the attributes and methods of its parent.
  It can **override** a method (write its own version) and call the parent version with `super()`.
- **Polymorphism**: `Car().drive()` and `Bicycle().drive()` use the same method name
  but give different results.
