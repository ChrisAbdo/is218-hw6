import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App().start()
    out, err = capfd.readouterr()
    assert "Goodbye!" in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App().start()
    out, err = capfd.readouterr()
    assert "No such command: unknown_command" in out
    assert "Goodbye!" in out

def test_app_add_command(capfd, monkeypatch):
    """Test the add command."""
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App().start()
    out, err = capfd.readouterr()
    assert "8" in out

def test_app_subtract_command(capfd, monkeypatch):
    """Test the subtract command."""
    inputs = iter(['subtract 10 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App().start()
    out, err = capfd.readouterr()
    assert "6" in out

def test_app_multiply_command(capfd, monkeypatch):
    """Test the multiply command."""
    inputs = iter(['multiply 6 7', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App().start()
    out, err = capfd.readouterr()
    assert "42" in out

def test_app_divide_command(capfd, monkeypatch):
    """Test the divide command."""
    inputs = iter(['divide 15 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App().start()
    out, err = capfd.readouterr()
    assert "5" in out

def test_app_menu_command(capfd, monkeypatch):
    """Test the menu command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App().start()
    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "add" in out
    assert "subtract" in out
    assert "multiply" in out
    assert "divide" in out
    assert "menu" in out
    assert "exit" in out