"""
This module contains tests for the calculator module.
"""

from decimal import Decimal
import pytest
from app import App
from app.calculator.calculations import Calculations

@pytest.fixture
def app():
    return App()

def test_addition(app, capfd, monkeypatch):
    """
    Test that the add command returns the expected result
    """
    inputs = iter(['add 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "5" in out

def test_subtraction(app, capfd, monkeypatch):
    """
    Test that the subtract command returns the expected result
    """
    inputs = iter(['subtract 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "2" in out

def test_multiplication(app, capfd, monkeypatch):
    """
    Test that the multiply command returns the expected result
    """
    inputs = iter(['multiply 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "6" in out

def test_division(app, capfd, monkeypatch):
    """
    Test that the divide command returns the expected result
    """
    inputs = iter(['divide 6 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "3" in out

def test_divide_by_zero(app, capfd, monkeypatch):
    """
    Test that dividing by zero raises an error message
    """
    inputs = iter(['divide 5 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "Cannot divide by zero" in out

def test_history(app, capfd, monkeypatch):
    """
    Test that the history contains the expected number of calculations
    """
    Calculations.clear_history()  # Clear history before the test
    inputs = iter(['add 1 1', 'subtract 5 3', 'multiply 2 4', 'divide 8 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    assert len(Calculations.history()) == 4

def test_clear_history(app):
    """
    Test that the history is cleared
    """
    Calculations.clear_history()
    assert len(Calculations.history()) == 0