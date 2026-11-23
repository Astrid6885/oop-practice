"""Inheritance - Problem 2: Person, Student and Employee."""


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"Hi, I am {self.name}, I am {self.age} and I live in {self.address}."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)  # reuse the parent constructor
        self.field_of_study = field_of_study

    def introduce(self):
        return f"{super().introduce()} I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return f"{super().introduce()} I work at {self.company}."


if __name__ == "__main__":
    people = [
        Person("Sam", 40, "Lyon"),
        Student("Lea", 20, "Cergy", "Data Science"),
        Employee("Tom", 35, "Paris", "Airbus"),
    ]
    for p in people:
        print(p.introduce())
