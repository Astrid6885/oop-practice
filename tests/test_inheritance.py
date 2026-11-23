from inheritance.vehicle import Vehicle, Car, Bicycle
from inheritance.person import Person, Student, Employee
from inheritance.bank_account import BankAccount, SavingsAccount


def test_vehicles():
    assert Vehicle().drive() == "Driving a vehicle"
    assert Car().drive() == "Driving a car"
    assert Bicycle().drive() == "Riding a bicycle"
    assert isinstance(Car(), Vehicle)


def test_people_introduce():
    student = Student("Lea", 20, "Cergy", "Data Science")
    employee = Employee("Tom", 35, "Paris", "Airbus")
    assert "Data Science" in student.introduce()
    assert "Airbus" in employee.introduce()
    assert isinstance(student, Person)


def test_deposit_and_withdraw():
    account = BankAccount("A", 100)
    assert account.deposit(50)
    assert account.balance == 150
    assert not account.withdraw(500)  # not enough money
    assert account.withdraw(100)
    assert account.balance == 50


def test_transfer():
    a = BankAccount("A", 100)
    b = BankAccount("B", 0)
    assert a.transfer(60, b) is True
    assert a.balance == 40 and b.balance == 60
    assert a.transfer(1000, b) is False
    assert a.balance == 40 and b.balance == 60  # nothing changed


def test_savings_account():
    s = SavingsAccount("S", 1000, interest_rate=0.05)
    assert s.add_interest() == 50
    assert s.check_balance() == 1050
    assert isinstance(s, BankAccount)
