import pytest
from Seventeenth import Employee

def test_give_default():
    Emp = Employee("Raouf","Benoud",1000)
    assert Emp.give_raise() == 6000
def test_give_custom_raise():
    Emp = Employee("Raouf","Benoud",1000)
    assert Emp.give_raise(1000) == 2000
