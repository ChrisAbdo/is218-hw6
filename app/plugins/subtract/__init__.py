from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.calculator import Calculator

class SubtractCommand(Command):
    def execute(self):
        try:
            num1 = Decimal(input("Enter first number: "))
            num2 = Decimal(input("Enter second number: "))
            result = Calculator.subtract(num1, num2)
            print(f"Result: {result}")
        except InvalidOperation:
            print("Invalid input. Please enter numeric values.")