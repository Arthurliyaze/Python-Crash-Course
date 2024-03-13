# 11.3 employee.py test file
import pytest
from chapter_11.employee import Employee

@pytest.fixture
def employee():
    """A function to create an employee"""
    employee = Employee('Arthur', 'Li', 80000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise works."""
    employee.give_raise()
    assert employee.salary == 80000 + 5000

def test_give_custom_raise(employee):
    """Test that a custom raise works"""
    employee.give_raise(6000)
    assert employee.salary == 80000 + 6000